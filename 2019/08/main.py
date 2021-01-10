import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod
from itertools import permutations, product

DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")


def read():
    with open(DIR / "input.txt") as f:
        t = f.read().split("\n")
    if t[-1] == "":
        t.pop()
    return np.array([int(i) for i in t[0]], dtype=np.int32).reshape(-1, 6, 25)


t = read()


def easy():
    m = (inf, 0)
    for i in range(100):
        c = len(np.where(t[i, :, :] == 0)[0])
        if c < m[0]:
            m = (c, i)
    print(prod([len(np.where(t[m[1], :, :] == k)[0]) for k in range(1, 3)]))


OCR = {
    422148690: "A",
    959335004: "B",
    422068812: "C",
    1024344606: "E",
    1024344592: "F",
    422074958: "G",
    623856210: "H",
    203491916: "J",
    625758866: "K",
    554189342: "L",
    959017488: "P",
    959017618: "R",
    623462988: "U",
    588583044: "Y",
    1008869918: "Z",
}


def ocr(t):
    c = OCR[int("".join([str(i) for i in t[:, :5].reshape(-1)]), 2)]
    if t.shape[1] > 5:
        c += ocr(t[:, 5:])
    return c


def hard():
    for l, y, x in product(*[range(n) for n in t.shape]):
        if l > 0:
            t[l, y, x] = t[l, y, x] if t[l - 1, y, x] == 2 else t[l - 1, y, x]
    print(ocr(t[-1]))


if __name__ == "__main__":
    easy()
    hard()