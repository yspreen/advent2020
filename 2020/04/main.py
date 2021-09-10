import re
import pathlib

DIR = pathlib.Path(__file__).parent.absolute()


def checktypes(kv):
    k = kv[:3]
    v = kv[4:]

    try:
        if k == "byr":
            return 1920 <= int(v) <= 2002
        if k == "iyr":
            return 2010 <= int(v) <= 2020
        if k == "eyr":
            return 2020 <= int(v) <= 2030
        if k == "hgt":
            if v[-2:] == "cm":
                return 150 <= int(v[:-2]) <= 193
            if v[-2:] == "in":
                return 59 <= int(v[:-2]) <= 76
        if k == "hcl":
            return re.match(r"^#[0-9a-f]{6}$", v)
        if k == "ecl":
            return v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if k == "pid":
            return re.match(r"^[0-9]{9}$", v)
    except:
        pass


def check(val):
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").replace(" ", "\n").split("\n\n")
    t = [l.splitlines() for l in t]

    required = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]

    n = 0
    for l in t:
        missing = set(required)
        for e in l:
            if val(e):
                missing.discard(e[:3])
        if len(missing) == 0:
            n += 1

    print(n)


def easy():
    check(lambda _: True)


def hard():
    check(checktypes)


if __name__ == "__main__":
    easy()
    hard()
