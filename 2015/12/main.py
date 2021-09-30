import pathlib
import json


def read():
    with open(DIR / "input") as f:
        return json.loads((f.read() if teststr == "" else teststr).splitlines()[0])


def count(obj, red=1):
    if isinstance(obj, dict):
        if not red and "red" in obj.values():
            return 0
        return sum(map(lambda i: count(i, red), obj.values()))
    if isinstance(obj, list):
        return sum(map(lambda i: count(i, red), obj))
    if isinstance(obj, int) or isinstance(obj, float):
        return obj
    return 0


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    print(count(t))
    print(count(t, red=0))
