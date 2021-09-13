import pathlib

with open(pathlib.Path(__file__).parent.absolute() / "input") as f:
    s = f.read()
print(s.count("(") - s.count(")"))
print([i for i in range(len(s)) if s[:i].count("(") - s[:i].count(")") == -1][0])
