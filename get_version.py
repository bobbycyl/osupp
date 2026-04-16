from System.Reflection import Assembly

assembly = Assembly.Load("osu.Game")
name = assembly.GetName()
version = name.Version

print(str(version))
