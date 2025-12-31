import re

from orjson import loads

from .core import JsonConvert


class Result(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        else:
            return 0.0


def re_deserialize(obj):
    return Result(loads(JsonConvert.SerializeObject(obj)))


def to_snake_case(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
