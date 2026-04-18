import os
import shutil
import sys
from pathlib import Path

from clr_loader import get_coreclr
from pythonnet import set_runtime

build_dir = os.path.join(
    os.environ["OSU_TOOLS_HOME"],
    "PerformanceCalculator",
    "bin",
    "Release",
    "net8.0",
)
runtime_config = os.path.join(
    build_dir,
    "PerformanceCalculator.runtimeconfig.json",
)
rt = get_coreclr(runtime_config=runtime_config)
set_runtime(rt)
sys.path.append(build_dir)


def _extract_stubs(output_dir):
    from stubgen.extract_stubs import extract_assemblies

    Path(output_dir).resolve().mkdir(exist_ok=True)
    _result = extract_assemblies(
        assembly_names=[
            "PerformanceCalculator",
            "osu.Game",
            "osu.Game.Rulesets.Osu",
            "osu.Game.Rulesets.Taiko",
            "osu.Game.Rulesets.Catch",
            "osu.Game.Rulesets.Mania",
        ],
        output_dir=Path(output_dir).resolve(),
        overwrite=False,
        skip_failed=False,
        multi_threaded=False,
    )


def _build_stubs(output_dir, stubs_dir):
    from stubgen.build_stubs import build_stubs

    _result = build_stubs(
        skeleton_files=list(Path(output_dir).glob("*_skeleton.json")),
        doc_files=list(Path(output_dir).glob("*_doc.json")),
        output_dir=Path(stubs_dir).resolve(),
        line_length=100,
        multi_threaded=False,
        format_files=False,
    )


def sync_stubs_to_src(stubs_dir, src_dir, blacklist):
    stubs_path = Path(stubs_dir)
    src_path = Path(src_dir)

    blacklist = set(blacklist)

    for item in stubs_path.rglob("*"):
        if item.suffix == ".py":
            continue
        rel_path = item.relative_to(stubs_path)

        if any(part in blacklist for part in rel_path.parts):
            continue

        target = src_path / rel_path

        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            # 自动补全 py.typed
            if rel_path.name.endswith("-stubs"):
                (target / "py.typed").touch()
                (target / "__init__.pyi").touch()
        else:
            # 确保父级目录存在并复制文件
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(item, target)


BLACKLIST = [
    "Audio",
    "Drawables",
    "Graphics",
    "IO",
    "IPC",
    "Input",
    "Localisation",
    "Online",
    "Overlays",
    "Screens",
    "Seasonal",
    "Skinning",
    "Storyboards",
    "Tests",
    "UI",
    "Updater",
    "Users",
    "__pycache__",
    "MessagePack-stubs",
    "PropertyChanged-stubs",
    "Sentry-stubs",
]
OUTPUT_DIR = "./output"
STUBS_DIR = "./stubs"
SRC_DIR = "./src"

_extract_stubs(OUTPUT_DIR)
_build_stubs(OUTPUT_DIR, STUBS_DIR)
sync_stubs_to_src(STUBS_DIR, SRC_DIR, BLACKLIST)
