import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return s[0], {k: v for k, v in map(lambda r: r.split(" -> "), s[2:])}


def easy():
    s = S
    for _ in range(10):
        i = 0
        while i < len(s) - 1:
            s = s[: i + 1] + R[s[i : i + 2]] + s[i + 1 :]
            i += 2
    counts = [s.count(i) for i in R.values()]
    print(max(counts) - min(counts))


def hard():
    r_ = r = {i: S.count(i) for i in R.keys()}
    n = {i: [] for i in R.keys()}
    for k, v in R.items():
        n[k] += [k[0] + v, v + k[1]]
    for _ in range(40):
        r, r_ = r_, {i: 0 for i in R.keys()}
        for k, v in r.items():
            for nk in n[k]:
                r_[nk] += v
    a = {v: 0 for _, v in R}
    for k, v in r_.items():
        a[k[0]] += v / 2
        a[k[1]] += v / 2
    a[S[0]] += 0.5
    a[S[-1]] += 0.5
    print(int(max(a.values())) - int(min(a.values())))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
S, R = read()
if __name__ == "__main__":
    easy()
    hard()
