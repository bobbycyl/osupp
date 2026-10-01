import re
from numbers import Number
from typing import Any, Literal

import clr
from System import Array, Byte, Object, Reflection
from System.IO import MemoryStream
from orjson import loads

from Newtonsoft.Json import JsonConvert
from PerformanceCalculator import ProcessorWorkingBeatmap
from osu.Game.Beatmaps import Beatmap
from osu.Game.Beatmaps.Formats import Decoder
from osu.Game.IO import LineBufferedReader

MOD_SETTING_TYPES = Literal["boolean", "number", "string", "enum"]


class Result(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        else:
            return None

    def _get_pure(self):
        return {k: v for k, v in self.items() if not k.startswith("__ek_")}


def re_deserialize(*, obj, **kwargs):
    return Result(
        loads(JsonConvert.SerializeObject(obj)),
        **{"__ek_%s" % k: v for k, v in kwargs.items()},
    )


def to_snake_case(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def validate_mod_setting_value(value, setting_type: MOD_SETTING_TYPES):
    match setting_type:
        case "boolean":
            return value is True or value is False
        case "number":
            # 由于 bool 是 int 的子类，这里需要判断是否不为 True or False
            return isinstance(value, Number) and value is not True and value is not False
        case "string" | "enum":
            return isinstance(value, str)
        case _:
            raise ValueError(f"unknown mod setting type: {setting_type}")


def processor_working_beatmap(py_bytes: bytes):
    reader = LineBufferedReader(MemoryStream(Array[Byte](py_bytes)))
    beatmap = Decoder.GetDecoder[Beatmap](reader).Decode(reader)  # type: ignore

    pwb_type = clr.GetClrType(ProcessorWorkingBeatmap)  # type: ignore
    beatmap_type = clr.GetClrType(Beatmap)  # type: ignore

    flags = Reflection.BindingFlags.NonPublic | Reflection.BindingFlags.Instance
    for c in pwb_type.GetConstructors(flags):
        params = c.GetParameters()
        if params.Length == 2 and params[0].ParameterType.IsAssignableFrom(beatmap_type):
            return c.Invoke(Array[Object]([beatmap, None]))

    raise RuntimeError("failed to get constructor")


def _is_int_str(v: str) -> bool:
    return v.isdecimal() or v[:1] == "-" and v[1:].isdecimal()


def make_unstandardized_mods_from_lines(*, slot: str | None = None, lines: str | None = None, mods: list[str] | None = None, mod_options: list[str] | None = None) -> list[dict[str, str | dict[str, str | float | bool]]]:
    """一个 Ruleset 不敏感、宽松的、自带 slot 的 mods 解析函数

    :param slot: slot 名，如 NM1
    :param lines: 多行文本，每一行的格式是 <acronym>_<mod_setting>=<value> 或 <acronym>
    :param mods: mod 列表，如 ["HD", "DT"]
    :param mod_options: mod_setting 列表，如 ["DT_speed_change=1.1"]
    :return: 一个未经类型验证和标准化的 mods 列表
    """
    if slot is not None:
        # slot 本身自带一个 mod
        auto_recognized_mod = slot[:2]
        # 最终期望得到：[{"acronym":<acronym>,"settings":{<mod_setting>:<value>}}]，如果不存在 settings，则不需要 settings 键
        # 先转换为 {acronym: [{mod_setting: value}]}，最后检测如果 settings 为空则不要添加该键
        mods_dict: dict[str, dict[str, Any]] = {auto_recognized_mod: {}}
    else:
        mods_dict: dict[str, dict[str, Any]] = {}

    if mods is None:
        mods = []
    if mod_options is None:
        mod_options = []
    if lines is None:
        lines = ""

    for line in lines.splitlines() + mods + mod_options:
        if line.strip():
            line_split = line.split("=", 1)
            if len(line_split) == 1:  # mod only
                mods_dict[line_split[0]] = mods_dict.get(line_split[0], {})
            else:  # mod with settings
                # 如果要设置 mod 参数，原则上要求 mod 本身已经加入
                # 但是为了方便起见，如果 mod 不存在，但又要求设置参数，则自动添加该 mod
                acronym_n_setting, value = line_split
                acronym, mod_setting = acronym_n_setting.split("_", 1)
                if acronym not in mods_dict:
                    mods_dict[acronym] = {}
                # 一个简单的类型推断与转换
                if value == "true":
                    value = True
                elif value == "false":
                    value = False
                elif _is_int_str(value):
                    value = int(value)
                elif "." in value and _is_int_str(value.replace(".", "", 1)):
                    value = float(value)
                else:
                    value = str(value)
                mods_dict[acronym].update({mod_setting: value})

    return [({"acronym": acronym, "settings": _settings} if _settings else {"acronym": acronym}) for acronym, _settings in mods_dict.items()]
