from osupp.core import init_osu_tools

init_osu_tools(r"C:\Users\bobbycyl\Projects\osu-tools\PerformanceCalculator\bin\Release\net8.0")

import System
from System.Reflection import Assembly

assembly = Assembly.Load("osu.Game")
name = assembly.GetName()
version = name.Version

print(str(version))
