import pathlib
from itertools import product

DIR = pathlib.Path(__file__).parent.absolute()


def get_masks(m):
    floating = m.count("X")
    floating_one = m.replace("0", "1")
    floating_zero = m.replace("1", "0")
    floating_or = int(m.replace("X", "0"), 2)
    masks = []
    if floating == 0:
        return [(int("1" * len(m), 2), floating_or)]
    for replacements in list(product("01", repeat=floating)):
        mask_one = int(floating_one.replace("X", "%s") % replacements, 2)
        mask_zero = int(floating_zero.replace("X", "%s") % replacements, 2)
        masks.append((mask_one, mask_zero | floating_or))
    return masks


def read():
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "")
    t = t.split("\n")
    if t[-1] == "":
        t.pop()
    t = [i.split(" ") for i in t]
    for i in t:
        if i[0] == "mask":
            i[1] = i[-1]
        else:
            i[0] = int(i[0][4:-1])
            i[1] = int(i[-1])
    t = [tuple(i[:2]) for i in t]

    return t


t = read()


def easy():
    m_or = 0
    m_and = 0
    mem = {}
    for cmd, param in t:
        if cmd == "mask":
            m_and = int(param.replace("X", "1"), 2)
            m_or = int(param.replace("X", "0"), 2)
            continue
        mem[cmd] = (param | m_or) & m_and
    print(sum(mem.values()))


def hard():
    masks = []
    mem = {}
    for cmd, param in t:
        if cmd == "mask":
            masks = get_masks(param)
            continue
        for m_and, m_or in masks:
            mem[(cmd & m_and) | m_or] = param
    print(sum(mem.values()))


if __name__ == "__main__":
    easy()
    hard()
