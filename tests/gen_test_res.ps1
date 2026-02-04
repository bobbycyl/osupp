$calculator = "C:/Users/bobbycyl/Projects/osu-tools/PerformanceCalculator/bin/Release/net8.0/PerformanceCalculator.dll"
dotnet $calculator difficulty -m HD -m DT -o DT_speed_change=1.3 3477131 -j > DIFF_RESULT.json
dotnet $calculator simulate osu -M 4 -G 34 -c 706 -L 0 -S 7 -X 2 3477131 -j > PERF_RESULT.json
dotnet $calculator simulate osu 3477131 -j > MAX_PP.json
dotnet $calculator simulate osu -m CL 3477131 -j > MAX_PP_CL.json
dotnet $calculator difficulty 4103079 -j > MANIA_DIFF_RESULT.json
dotnet $calculator difficulty -r:1 3477131 -j > CONVERTED_TAIKO_DIFF_RESULT.json
dotnet $calculator simulate taiko 4434797 -G 24 -c 272 -X 2 -j > TAIKO_SCORE_RESULT.json
dotnet $calculator simulate catch 2158794 -c 226 -X 7 -D 28 -T 162 -m NF -m CL -j > CATCH_SCORE_RESULT.json
dotnet $calculator simulate mania -G 55 -X 1 -T 403 4364723 -j > MANIA_SCORE_RESULT.json
dotnet $calculator simulate mania -M 5 -G 190 -O 20 -T 1199 -X 10 -m CL 767046 -j > MANIA_CL_SCORE_RESULT.json
dotnet $calculator mods > osu_mods.json
