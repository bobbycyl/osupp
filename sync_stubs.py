import shutil
from pathlib import Path


def sync_stubs_to_src(stubs_root, src_root, blacklist):
    stubs_path = Path(stubs_root)
    src_path = Path(src_root)

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


BLACKLIST = ['Audio', 'Drawables', 'Graphics', 'IO', 'IPC', 'Input', 'Localisation', 'Online', 'Overlays', 'Screens', 'Seasonal', 'Skinning', 'Storyboards', 'Tests', 'UI', 'Updater', 'Users', '__pycache__']

sync_stubs_to_src("./stubs", "./src", BLACKLIST)
