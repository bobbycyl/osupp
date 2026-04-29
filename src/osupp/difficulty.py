from typing import Any, Iterable, Literal, Optional, TypedDict, cast

import System
from System import Array, OperationCanceledException

from PerformanceCalculator import LegacyHelper, ProcessorCommand, ProcessorWorkingBeatmap
from osu.Game.Configuration import SettingSourceExtensions
from osu.Game.Rulesets import Ruleset
from osu.Game.Rulesets.Mods import Mod
from .util import MOD_SETTING_TYPES, Result, re_deserialize, to_snake_case


class ModSetting(TypedDict):
    Name: str
    Type: MOD_SETTING_TYPES
    Label: str
    Description: str
    UnderlyingValue: Optional[Any]
    Default: Optional[Any]
    IsInteger: Optional[bool]
    DefaultPrecision: Optional[int | float]
    EnumValues: Optional[list[str]]


class ModEntry(TypedDict):
    Acronym: str
    Name: str
    Description: str
    Type: Literal["DifficultyReduction", "DifficultyIncrease", "Automation", "Conversion", "Fun", "System"]
    Settings: list[ModSetting]


def get_all_mods(ruleset: Ruleset) -> list[ModEntry]:
    all_mods_data: list[ModEntry] = []
    all_mods = ruleset.CreateAllMods()
    for mod in all_mods:
        mod = cast(Mod, mod)
        settings_data: list[ModSetting] = []
        source_properties = cast(
            Iterable,
            SettingSourceExtensions.GetSettingsSourceProperties(mod),
        )
        for setting in source_properties:
            settings_source, property_info = setting.Item1, setting.Item2
            bindable = property_info.GetValue(mod)
            assert bindable is not None
            i_bindable = bindable.GetType().GetInterface("IBindable`1")
            if i_bindable:
                net_type = i_bindable.GetGenericArguments()[0]
            else:
                net_type = bindable.GetType()
            json_type_extended = get_json_type(net_type)

            _enum_values = [str(x) for x in System.Enum.GetValues(net_type)] if json_type_extended == "enum" else None
            _underlying_value = SettingSourceExtensions.GetUnderlyingSettingValue(bindable)
            _default = getattr(bindable, "Default", None)
            _is_integer = None
            _default_precision = None
            if json_type_extended == "enum":
                # 处理为字符串
                _underlying_value = str(_underlying_value)
                _default = str(_default) if _default is not None else None
            elif json_type_extended == "number":
                _is_integer = getattr(bindable, "IsInteger", None)
                _default_precision = getattr(bindable, "DefaultPrecision", None)
                if _default_precision is not None:
                    _default_precision = round(_default_precision, 2)  # type: ignore

            name = to_snake_case(property_info.Name)
            settings_data.append(
                ModSetting(
                    Name=name,
                    Type=json_type_extended,
                    Label=str(settings_source.Label),
                    Description=str(settings_source.Description),
                    UnderlyingValue=_underlying_value,
                    Default=_default,
                    IsInteger=_is_integer,
                    DefaultPrecision=_default_precision,
                    EnumValues=_enum_values,
                ),
            )
        # 组装 acronym 和 settings
        mod_entry = ModEntry(
            Acronym=mod.Acronym,
            Name=mod.Name,
            Description=str(mod.Description),
            Type=cast(Literal["DifficultyReduction", "DifficultyIncrease", "Automation", "Conversion", "Fun", "System"], str(mod.Type)),
            Settings=settings_data,
        )
        all_mods_data.append(mod_entry)

    return all_mods_data


# 扩展了 ModsCommand.cs 的 getJsonType 私有方法
def get_json_type(net_type) -> MOD_SETTING_TYPES:
    if net_type is None:
        return "string"

    # 剥离泛型参数，即把 int?, float? double? bool? 的 ? 拿掉
    if net_type.IsGenericType and net_type.GetGenericTypeDefinition().Name == "Nullable`1":
        net_type = net_type.GetGenericArguments()[0]
    full_name = net_type.FullName

    if full_name in ("System.Byte",
            "System.SByte",
            "System.Int16", "System.UInt16",
            "System.Int32", "System.UInt32",
            "System.Int64", "System.UInt64",
            "System.IntPtr", "System.UIntPtr",
        "System.Double",
        "System.Single",
        "System.Decimal",
    ):
        return "number"
    if full_name == "System.Boolean":
        return "boolean"
    if full_name == "System.String":
        return "string"
    if net_type.IsEnum:
        return "enum"

    raise TypeError(f"unknown type: {net_type}")


def calculate_difficulty(
    beatmap_path: str,
    mods: Optional[list[str]] = None,
    mod_options: Optional[list[str]] = None,
    ruleset_id: Optional[Literal[0, 1, 2, 3]] = None,
) -> Result:
    working_beatmap = ProcessorWorkingBeatmap(beatmap_path)
    if ruleset_id is None:
        ruleset_id: Literal[0, 1, 2, 3] = cast(
            Literal[0, 1, 2, 3],
            working_beatmap.BeatmapInfo.Ruleset.OnlineID,
        )
    ruleset = LegacyHelper.GetRulesetFromLegacyID(ruleset_id)
    calculator = ruleset.CreateDifficultyCalculator(working_beatmap)

    if mods is None:
        mods = []
    if mod_options is None:
        mod_options = []
    mod_array = ProcessorCommand.ParseMods(
        ruleset,
        Array[str](mods),
        Array[str](mod_options),
    )

    try:
        return re_deserialize(obj=calculator.Calculate(mod_array))
    except OperationCanceledException:  # ty:ignore[invalid-exception-caught]
        return Result({})
