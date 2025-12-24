# osupp

## 简介

简单复刻了 [PerformanceCalculator](https://github.com/ppy/osu-tools/blob/master/PerformanceCalculator) 的常用功能。

目前仅完成了 Standard 模式。

## 使用方法

1. 安装 Python 3.12、.Net 8.0、pythonnet 和本仓库的 osupp 包
2. 本地克隆 [osu-tools](https://github.com/ppy/osu-tools) 仓库

   ```shell
   git clone https://github.com/ppy/osu-tools.git
   ```

3. 编译 PerformanceCalculator

   ```shell
   cd osu-tools/PerformanceCalculator
   dotnet build -c Release
   ```

4. 在 Python 中初始化 .Net 运行时

   ```python
   from osupp.core import init_osu_tools
   init_osu_tools(r"path/to/osu-tools/PerformanceCalculator/bin/Release/net8.0")
   ```

已经封装了常用函数，但与 rosu-pp 的使用习惯不同，与 osu-tools CLI 的使用习惯相近。
