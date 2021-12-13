import numpy as np
import re
import pathlib
import json
from functools import reduce
from string import ascii_lowercase
from math import prod, gcd, sqrt
from itertools import permutations, product
from llist import dllist as llist
from copy import deepcopy
from hashlib import md5, sha256


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).split("\n\n")
        s, ins = s[0].splitlines(), s[1].replace("fold along ", "").splitlines()
    pairs = np.array(lmap(lambda r: lmap(int, r.split(",")), s))
    A = np.zeros((pairs[:, 0].max() + 1, pairs[:, 1].max() + 1))
    for x, y in pairs:
        A[x, y] = 1
    return A, lmap(lambda i: (i[0], int(i[2:])), ins)


def step(axis, fold):
    global A
    if axis == "x":
        if fold * 2 > A.shape[0] - 1:
            A = np.pad(A, ((0, fold * 2 - A.shape[0] + 1), (0, 0)))
        A = A[:fold, :] + np.flip(A[fold + 1 :, :], 0)
    if axis == "y":
        if fold * 2 > A.shape[1] - 1:
            A = np.pad(A, ((0, 0), (0, fold * 2 - A.shape[1] + 1)))
        A = A[:, :fold] + np.flip(A[:, fold + 1 :], 1)
    A[A > 1] = 1


def easy():
    step(*ins[0])
    print(int(A.sum()))


def OCR(A):
    from PIL import Image
    import pytesseract

    img = Image.new("RGB", A.shape)
    pixels = img.load()
    for y in range(A.shape[1]):
        for x in range(0, A.shape[0]):
            pixels[x, y] = (0, 0, 0) if A.T[y, x] else (255, 255, 255)
    img = img.resize((A.shape[0] * 2, A.shape[1] * 2), Image.NEAREST)
    img = img.resize((A.shape[0] * 50, A.shape[1] * 50), Image.BILINEAR)
    return pytesseract.image_to_string(img).strip()


def hard():
    for i in ins[1:]:
        step(*i)
    # print(A.T)
    print(OCR(np.pad(A, ((2, 2), (2, 2)))))


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
A, ins = read()
if __name__ == "__main__":
    easy()
    hard()
