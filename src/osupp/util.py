import re
from numbers import Number
from typing import Literal

from orjson import loads

from .core import JsonConvert


class Result(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        else:
            return 0.0

    def _get_pure(self):
        return {k: v for k, v in self.items() if not k.startswith("__ek_")}


def re_deserialize(obj, **kwargs):
    return Result(
        loads(JsonConvert.SerializeObject(obj)),
        **{"__ek_%s" % k: v for k, v in kwargs.items()},
    )


def to_snake_case(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def validate_mod_setting_value(value, setting_type: Literal["boolean", "number", "string"]):
    match setting_type:
        case "boolean":
            return value is True or value is False
        case "number":
            # 由于 bool 是 int 的子类，这里需要判断是否不为 True or False
            return isinstance(value, Number) and value is not True and value is not False
        case "string":
            return isinstance(value, str)
        case _:
            raise ValueError(f"unknown mod setting type: {setting_type}")
