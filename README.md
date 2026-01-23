# osupp

## 简介

简单地包装了 [PerformanceCalculator](https://github.com/ppy/osu-tools/blob/master/PerformanceCalculator) 的常用功能。

目前已完成所有 4 个模式。

## 使用方法

1. 安装 Python 3.12、.NET 8.0、pythonnet 和本仓库的 osupp 包
2. 本地克隆 [osu](https://github.com/ppy/osu) 和 [osu-tools](https://github.com/ppy/osu-tools) 仓库，
   并对 osu 仓库应用 [patch](https://github.com/bobbycyl/osu-patch)

   ```shell
   git clone https://github.com/ppy/osu.git
   git clone https://github.com/ppy/osu-tools.git
   git clone https://github.com/bobbycyl/osu-patch.git
   cd osu
   git checkout 2025.1007.0
   git apply ../osu-patch/strain_timeline.patch
   ```

3. 使用本地 osu! 源码编译 PerformanceCalculator

   在 Windows 上执行 `UseLocalOsu.ps1`，在其它系统上执行 `UseLocalOsu.sh`

   ```shell
   dotnet build -c Release
   ```

4. 在 Python 中初始化 .NET 运行时

   ```python
   from osupp.core import init_osu_tools
   init_osu_tools(r"path/to/osu-tools/PerformanceCalculator/bin/Release/net8.0")
   ```

已经封装了常用函数，并一定程度上模仿了 rosu-pp 的使用习惯。

## 注意事项

1. 当前测试 osu! 版本号：`2025.1007.0.0`
2. [osu_mods](./tests/osu_mods.json) 文件为 osu-tools 导出的所有模组信息
3. 可以使用 `set_config` 来控制是否启用依赖 patch 的功能，全部关闭之后即便使用原版 osu-tools 程序也能正常运行
