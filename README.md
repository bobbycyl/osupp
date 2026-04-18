# osupp

## 简介

简单地包装了 [PerformanceCalculator](https://github.com/ppy/osu-tools/blob/master/PerformanceCalculator) 的常用功能。

目前已完成所有 4 个模式，借助 [stubgen](https://github.com/Mimer29or40/pythonnet-stubs) 对 PerformanceCalculator 和 osu
生成常用存根文件以实现代码提示。

如果 osu! 或 osu-tools 发生了重大更新，欢迎开 issue 或 pull request 交流。

## 使用方法

### 1. 安装 Python 3.12、.NET 8.0 和本仓库的 osupp 包

### 2. 本地克隆 [osu-tools](https://github.com/ppy/osu-tools) 和 [osu](https://github.com/ppy/osu) （可选）仓库

```shell
git clone https://github.com/ppy/osu-tools.git
git clone https://github.com/ppy/osu.git  # 可选
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

执行 `sync_stubs.py` 生成常用存根文件。

注1：有些存根文件的生成会有问题，需要手动修复；

注2：由于 `Newtonsoft.Json` 和 `PerformanceCalculatorGUI` 通常用不到，
故本包仅针对使用到的类和函数做了最小化的存根文件，以供类型注解用。

### 生成测试结果

[测试结果生成脚本](./tests/gen_test_res.ps1) 通过外部调用 osu-tools 生成测试结果。

## 注意事项

1. 当前测试 osu! 版本号：`2026.317.0.0`
2. 目前须通过环境变量来指定 osu-tools 的路径。
3. [osu_mods](./tests/osu_mods.json) 文件为 osu-tools 导出的所有模组信息
