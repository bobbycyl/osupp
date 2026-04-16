$calculator = $env:OSU_TOOLS_HOME + "\PerformanceCalculator\bin\Release\net8.0\PerformanceCalculator.dll"
dotnet $calculator difficulty -m HD -m DT -o DT_speed_change=1.3 3477131 -j > DIFF_RESULT.json
dotnet $calculator simulate osu --mehs 4 --goods 34 --combo 706 --large-tick-misses 0 --slider-tail-misses 7 --misses 2 3477131 -j > PERF_RESULT.json
dotnet $calculator simulate osu 3477131 -j > MAX_PP.json
dotnet $calculator simulate osu -m CL 3477131 -j > MAX_PP_CL.json
dotnet $calculator difficulty 4103079 -j > MANIA_DIFF_RESULT.json
dotnet $calculator difficulty -r:1 3477131 -j > CONVERTED_TAIKO_DIFF_RESULT.json
dotnet $calculator simulate taiko 4434797 --goods 24 --combo 272 --misses 2 -j > TAIKO_SCORE_RESULT.json
dotnet $calculator simulate catch 2158794 --combo 226 --misses 7 --droplets 28 --tiny-droplets 162 -m NF -m CL -j > CATCH_SCORE_RESULT.json
dotnet $calculator simulate mania --goods 55 --misses 1 --greats 403 4364723 -j > MANIA_SCORE_RESULT.json
dotnet $calculator simulate mania --mehs 5 --goods 190 --oks 20 --greats 1199 --misses 10 -m CL 767046 -j > MANIA_CL_SCORE_RESULT.json
dotnet $calculator mods > osu_mods.json
