from typing import Literal

import orjson

from osupp.core import init_osu_tools

init_osu_tools(
    r"C:\Users\bobbycyl\Projects\osu-tools\PerformanceCalculator\bin\Release\net8.0",
)
from osupp.difficulty import ModEntry, get_all_mods  # noqa: E402
from osupp.core import (  # noqa: E402
    OsuRuleset,
    CatchRuleset,
    ManiaRuleset,
    TaikoRuleset,
)


def mod_setting_type_mapping(mods_info: list[ModEntry]) -> dict[str, dict[str, Literal["boolean", "number", "string"]]]:
    d = {}
    for mod_info in mods_info:
        mod_acronym = mod_info["Acronym"]
        mod_settings = mod_info["Settings"]
        md = {}
        for mod_setting in mod_settings:
            mod_setting_name = mod_setting["Name"]
            mod_setting_type = mod_setting["Type"]
            md[mod_setting_name] = mod_setting_type
        d[mod_acronym] = md
    return d


def test():
    ruleset_mapping = {
        0: OsuRuleset,
        1: TaikoRuleset,
        2: CatchRuleset,
        3: ManiaRuleset,
    }
    for i, ruleset in ruleset_mapping.items():
        mods_info = get_all_mods(ruleset())
        mod_setting_type_d = mod_setting_type_mapping(mods_info)
        with open("osu_mods.json", "rb") as fi_b:
            osu_mods_osu_tool = orjson.loads(fi_b.read())[i]["Mods"]
        for osu_mod_osu_tool in osu_mods_osu_tool:
            osu_mod_acronym = osu_mod_osu_tool["Acronym"]
            osu_mod_settings = osu_mod_osu_tool["Settings"]
            for osu_mod_setting in osu_mod_settings:
                osu_mod_setting_name = osu_mod_setting["Name"]
                osu_mod_setting_type = osu_mod_setting["Type"]
                assert mod_setting_type_d[osu_mod_acronym][osu_mod_setting_name] == osu_mod_setting_type
