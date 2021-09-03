import numpy as np
import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = f.read() if teststr == "" else teststr
    return np.array(lmap(lambda r: lmap(ord, r), s.splitlines()), int)


def right(p):
    return (p[1], -p[0])


def left(p):
    return right(right(right(p)))


def easy():
    t[t == 32] = 0
    for c in "-|+":
        t[t == ord(c)] = 1
    p, d, s, n = (1, np.where(t[0] > 0)[0][0]), DOWN, "", 2

    while True:
        forward = (p[0] + d[0], p[1] + d[1])
        if t[forward] == 0:
            r = right(d)
            l = left(d)
            f_r = (p[0] + r[0], p[1] + r[1])
            f_l = (p[0] + l[0], p[1] + l[1])
            if t[f_r] != 0:
                d = r
            elif t[f_l] != 0:
                d = l
            else:
                return print(s, n, sep="\n")
        else:
            p, n = forward, n + 1
            if t[p] > 1:
                s += chr(t[p])


def hard():
    return


teststr = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
                """
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
DOWN = (1, 0)
if __name__ == "__main__":
    easy()
    hard()
