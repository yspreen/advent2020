import pathlib
from math import prod


def read():
    with open(DIR / "input") as f:
        return (f.read() if teststr == "" else teststr).splitlines()[0]


def next_bit():
    for c in t:
        num = int(c, 16)
        for m in [8, 4, 2, 1]:
            yield 1 if (num & m) > 0 else 0


def take(n, bits):
    return [next(bits) for _ in range(n)]


def num(bits):
    n = 0
    for i in bits:
        n <<= 1
        n += i
    return n


def decipher_package(bits):
    global V
    V += num(take(3, bits))
    t = num(take(3, bits))

    if t == 4:
        first_bit = 1
        n = []
        while first_bit:
            first_bit = num(take(1, bits))
            n += take(4, bits)
        return num(n)
    length_type = num(take(1, bits))
    length = num(take(15, bits)) if length_type == 0 else num(take(11, bits))
    packets = []
    if length_type == 0:
        sub = iter(take(length, bits))
        while True:
            try:
                packets.append(decipher_package(sub))
            except:
                break
    else:
        for _ in range(length):
            packets.append(decipher_package(bits))
    return [
        lambda p: sum(p),
        lambda p: prod(p),
        lambda p: min(p),
        lambda p: max(p),
        None,
        lambda p: 1 if p[0] > p[1] else 0,
        lambda p: 1 if p[0] < p[1] else 0,
        lambda p: 1 if p[0] == p[1] else 0,
    ][t](packets)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t, V = read(), 0
if __name__ == "__main__":
    val = decipher_package(next_bit())
    print(V, val, sep="\n")
