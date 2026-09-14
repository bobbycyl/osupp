$dll = Join-Path $env:OSU_TOOLS_HOME "PerformanceCalculator\bin\Release\net10.0\osu.Game.dll"
[System.Reflection.AssemblyName]::GetAssemblyName($dll).Version.ToString()
