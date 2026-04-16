# osupp

## 简介

简单地包装了 [PerformanceCalculator](https://github.com/ppy/osu-tools/blob/master/PerformanceCalculator) 的常用功能。

目前已完成所有 4 个模式，借助 [stubgen](https://github.com/Mimer29or40/pythonnet-stubs) 对 PerformanceCalculator 和 osu
生成常用存根文件以实现代码提示。

如果 osu! 或 osu-tools 发生了重大更新，欢迎开 issue 或 pull request 交流。

## 使用方法

### 1. 安装 Python 3.12、.NET 8.0 和本仓库的 osupp 包

### 2. 本地克隆 [osu](https://github.com/ppy/osu) 和 [osu-tools](https://github.com/ppy/osu-tools) 仓库

```shell
git clone https://github.com/ppy/osu.git
git clone https://github.com/ppy/osu-tools.git
```

### 3. 添加环境变量

设置环境变量 `OSU_TOOLS_HOME`，指向 osu-tools 目录。

### 4. 编译 PerformanceCalculator 和 PerformanceCalculatorGUI

可选：在 Windows 上执行 `UseLocalOsu.ps1`，在其它系统上执行 `UseLocalOsu.sh` 以使用本地 osu! 源码编译
PerformanceCalculator

分别在 `PerformanceCalculator` 和 `PerformanceCalculatorGUI` 目录下执行：

```shell
dotnet build -c Release
```

## 开发与贡献

### 生成存根文件

由于 PerformanceCalculator 是一个独立的 .NET 项目，因此需要魔改 `stubgen`。

具体而言，在 `stubgen/extract_stubs.py` 中，`import clr` 之前添加以下代码：

```python
import os
import sys
from clr_loader import get_coreclr
from pythonnet import set_runtime

build_dir = r"path/to/osu-tools/PerformanceCalculator/bin/Release/net8.0"
runtime_config = os.path.join(
    build_dir, "PerformanceCalculator.runtimeconfig.json",
)
rt = get_coreclr(runtime_config=runtime_config)
set_runtime(rt)
sys.path.append(build_dir)
```

然后执行 `stubgen`：

```shell
python -m stubgen -o output extract PerformanceCalculator osu.Game osu.Game.Rulesets.Osu osu.Game.Rulesets.Taiko osu.Game.Rulesets.Catch osu.Game.Rulesets.Mania
python -m stubgen -o stubs build output/*_skeleton.json output/*_doc.json
```

最后执行 `sync_stubs.py` 复制常用存根文件。

### 生成测试结果

[测试结果生成脚本](./tests/gen_test_res.ps1) 通过外部调用 osu-tools 生成测试结果。

## 注意事项

1. 当前测试 osu! 版本号：`2026.317.0.0`
2. 目前须通过环境变量来指定 osu-tools 的路径。
3. [osu_mods](./tests/osu_mods.json) 文件为 osu-tools 导出的所有模组信息
