from typing import Literal, Optional

from .core import Array, LegacyHelper, OperationCanceledException, ProcessorCommand, ProcessorWorkingBeatmap, Ruleset, SettingSourceExtensions, System
from .util import Result, re_deserialize, to_snake_case


def get_all_mods(ruleset: Ruleset) -> list[dict[str, str | list[dict[str, str | type[str | float | bool]]]]]:
    all_mods_data: list[dict[str, str | list[dict[str, str | type[str | float | bool]]]]] = []
    all_mods = ruleset.CreateAllMods()
    all_mods_list = list(all_mods)
    for mod in all_mods_list:
        settings_data: list[dict[str, str | type[str | float | bool]]] = []
        source_properties = SettingSourceExtensions.GetSettingsSourceProperties(mod)
        for setting in source_properties:
            settings_source, property_info = setting.Item1, setting.Item2
            bindable = property_info.GetValue(mod)
            assert bindable is not None
            i_bindable = bindable.GetType().GetInterface("IBindable`1")
            if i_bindable:
                net_type = i_bindable.GetGenericArguments()[0]
            else:
                net_type = bindable.GetType()
            py_type = transform_net_type(net_type)

            name = to_snake_case(property_info.Name)
            settings_data.append(
                {
                    "Name": name,
                    "Type": py_type,
                    "Label": str(settings_source.Label),
                    "Description": str(settings_source.Description),
                },
            )

        # 组装 acronym 和 settings
        mod_entry = {
            "Acronym": mod.Acronym,
            "Settings": settings_data,
        }

        all_mods_data.append(mod_entry)

    return all_mods_data


def transform_net_type(net_type) -> type[str | float | bool]:
    if net_type is None:
        return str

    # 剥离泛型参数，即把 int?, float? double? bool? 的 ? 拿掉
    if net_type.IsGenericType and net_type.GetGenericTypeDefinition().Name == "Nullable`1":
        net_type = net_type.GetGenericArguments()[0]
    full_name = net_type.FullName

    if full_name in ["System.Int32", "System.Double", "System.Single", "System.Decimal"]:
        return float
    if full_name == "System.Boolean":
        return bool
    if full_name == "System.String":
        return str
    if net_type.IsEnum:
        return str

    raise TypeError(f"unknown type: {net_type}")


def calculate_difficulty(beatmap_path: str, mods: Optional[list[str]] = None, mod_options: Optional[list[str]] = None, ruleset_id: Optional[Literal[0, 1, 2, 3]] = None) -> Result:
    working_beatmap = ProcessorWorkingBeatmap(beatmap_path)
    if ruleset_id is None:
        ruleset_id = working_beatmap.BeatmapInfo.Ruleset.OnlineID
    ruleset = LegacyHelper.GetRulesetFromLegacyID(ruleset_id)
    calculator = ruleset.CreateDifficultyCalculator(working_beatmap)

    if mods is None:
        mods = []
    if mod_options is None:
        mod_options = []
    mod_array = ProcessorCommand.ParseMods(ruleset, Array[str](mods), Array[str](mod_options))

    try:
        return re_deserialize(calculator.Calculate(mod_array))
    except OperationCanceledException:
        return Result({})
