from orjson import loads

from .core import JsonConvert


def re_deserialize(obj):
    return loads(JsonConvert.SerializeObject(obj))
