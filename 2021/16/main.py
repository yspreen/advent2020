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
    if t == 0:
        return sum(packets)
    if t == 1:
        return prod(packets)
    if t == 2:
        return min(packets)
    if t == 3:
        return max(packets)
    if t == 5:
        return 1 if packets[0] > packets[1] else 0
    if t == 6:
        return 1 if packets[0] < packets[1] else 0
    if t == 7:
        return 1 if packets[0] == packets[1] else 0


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
t, V = read(), 0
if __name__ == "__main__":
    val = decipher_package(next_bit())
    print(V, val, sep="\n")
