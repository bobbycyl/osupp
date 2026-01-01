import orjson

from osupp.core import init_osu_tools
init_osu_tools(r"C:\Users\bobbycyl\Projects\osu-tools\PerformanceCalculator\bin\Release\net8.0")
from osupp.difficulty import get_all_mods
from osupp.core import OsuRuleset, CatchRuleset, ManiaRuleset, TaikoRuleset


def mod_setting_type_mapping(mods_info: list[dict[str, str | list[dict[str, str | type[str | float | bool]]]]]) -> dict[str, dict[str, type[str | float | bool]]]:
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
        print(mods_info)
        mod_setting_type_d = mod_setting_type_mapping(mods_info)
        with open("osu_mods.json", "rb") as fi_b:
            osu_mods_net = orjson.loads(fi_b.read())[i]["Mods"]
        type_mapping = {
            bool: "boolean",
            int: "number",
            float: "number",
            str: "string",
        }
        for osu_mod_net in osu_mods_net:
            osu_mod_acronym = osu_mod_net["Acronym"]
            osu_mod_settings = osu_mod_net["Settings"]
            for osu_mod_setting in osu_mod_settings:
                osu_mod_setting_name = osu_mod_setting["Name"]
                osu_mod_setting_type = osu_mod_setting["Type"]
                assert type_mapping[mod_setting_type_d[osu_mod_acronym][osu_mod_setting_name]] == osu_mod_setting_type
