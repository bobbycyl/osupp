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
