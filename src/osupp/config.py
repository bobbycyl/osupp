_CONFIG = {
    "strain_timeline": True,
}


def set_config(**kwargs):
    global _CONFIG
    for key, value in kwargs.items():
        _CONFIG[key] = value


def get_config(key=None):
    if key is None:
        return _CONFIG.copy()
    return _CONFIG.get(key)
