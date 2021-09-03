import numpy as np
import pathlib
from string import ascii_lowercase


def read(n=1):
    with open(DIR / "input") as f:
        t = [[replacements[i] for i in sub] for sub in f.read().split("\n")][:-1]
    return np.array(t, np.int32)


def neighbors(pos):
    n = []
    for d in directions:
        n.append((pos[0] + d[0], pos[1] + d[1]))
    return n


def bfs(c=0, initial=True, transparent=0):
    pos = c_pos(c)
    # t[np.where(t == -2)] = 0

    cost = {pos: 0}
    chain = {pos: []}
    visited = set([pos])
    goal = [pos]
    chain_starts = set()

    while goal:
        pos = goal.pop(0)
        for n in neighbors(pos):
            if n in visited or t[n] == -1:
                continue
            cost[n] = cost[pos] + 1
            if initial:
                chain[n] = list(chain[pos])
                if t[n] > 0:
                    if not chain[n]:
                        chain_starts.add(t[n])
                    chain[n].append(t[n])
            elif t[n] > 0 and t[n] != transparent:
                continue
            goal.append(n)
            visited.add(n)
    if not initial:
        return cost
    return cost, chain, chain_starts


class Letter:
    items = {}

    def __init__(self, c, parent):
        if self.items.get(c, None) is not None:
            return
        self.items[c] = self
        self.c = c
        self.parent = parent
        self.children = []
        self.req = set()
        try:
            self.items[parent].children.append(c)
        except:
            pass

    def calc(self, cost, parent_req=set()):
        # add all path requirements
        self.req |= parent_req
        if self.parent is not None and self.parent >= 100:
            self.req.add(self.parent - 100)

        # set distances to children
        for c in self.children:
            distances[(self.c, c)] = distances[(c, self.c)] = (
                cost[c_pos(c)] - cost[c_pos(self.c)]
            )

        # find same layer neighbors with bfs
        if len(self.children) > 1:
            for c in self.children:
                ds = bfs(c, False, self.c)
                for o in self.children:
                    op = c_pos(o)
                    distances[(c, o)] = distances[(o, c)] = ds[op]

        # inherit distances of parent
        if self.parent != 0 and self.parent != None:
            pd = distances[(self.c, self.parent)]
            for k, v in list(distances.items()):
                if self.parent in k and self.c not in k:
                    k = k[0] if self.parent == k[1] else k[1]
                    if distances.get((self.c, k), None) is not None:
                        continue
                    distances[(self.c, k)] = distances[(k, self.c)] = v + pd

        # calculate children distances
        _ = [self.items[c].calc(cost, self.req) for c in self.children]


def c_pos(c):
    c = -2 if c == 0 else c
    return tuple(map(lambda i: i[0], np.where(t == c)))


def sub_paths(p):
    if PART == 1:
        return [p]
    sub = [[] for _ in range(4)]
    for i in p:
        sub[quadrant(i)].append(i)
    return sub


def optimal(paths, chain=[]):
    skip = len(chain) - 1 if chain and PART == 1 else 0
    m = (inf, 0)
    for p_ in paths:
        c = 0
        p = p_[skip:]
        for p in sub_paths(p):
            for i in range(1, len(p)):
                c += distances[(p[i], p[i - 1])]
        if c < m[0]:
            m = (c, p_)
    return m


def options(seen, next, chain, pr=0):
    if not next:
        return [chain]
    next.sort()
    key = tuple(chain[-1:] + [-1] + sorted(next) + [-1] + sorted(list(seen)))
    c = cache.get(key, None)
    if c is not None:
        chain = chain + c
        return [chain]
    opt = []
    for n in next:
        if pr:
            print(".")
        chain_ = chain + [n]
        seen_ = seen | set([n])
        next_ = [i for i in next if i != n]
        for i in Letter.items.values():
            if i.c >= 100:
                continue
            if i.c in seen_:
                continue
            if i.c in next_:
                continue
            if not (i.req - seen_):
                next_ += [i.c]
        n = options(seen_, next_, chain_)
        opt.extend(n)
    result = optimal(opt, chain)[1]
    cache[key] = result[len(chain) :]
    return [result]


def easy():
    global distances
    cost, chain, chain_starts = bfs()

    # print(chain)
    # print(rev_replacements[12])
    # print(rev_replacements[101])

    # print(list(map(lambda i: rev_replacements[i], chain_starts)))

    chains = map(lambda i: c_pos(i + 1), list(range(N)) + list(range(100, N + 100)))
    # print((43, 27) in list(chains))
    chains = list(chain.values())
    chains = {k: sorted([i for i in chains if k in i]) for k in chain_starts}
    for k, v in chains.items():
        for cs in v:
            cs = [0] + cs
            for i in range(1, len(cs)):
                Letter(cs[i], cs[i - 1])
    start = Letter.items[0]
    start.calc(cost)

    # print(list(map(lambda a: rev_replacements[a], Letter.items[replacements["h"]].req)))
    distances = {k: v for k, v in distances.items() if sum(k) < 100}
    shortest(start)


def shortest(start):
    opt = options(
        set([0] if PART == 1 else imaginaries + [0]),
        [c for c in start.children if c < 100 and not Letter.items[c].req],
        [0] if PART == 1 else imaginaries,
    )
    opt = optimal(opt)
    # print([rev_replacements[i] for i in opt[1]])
    print(opt[0])


def quadrant(pos):
    if pos in imaginaries:
        return imaginaries.index(pos)
    pos = pos if isinstance(pos, tuple) else c_pos(pos)
    q = 0
    if pos[0] > M:
        q += 1
    if pos[1] > M:
        q += 2
    return q


def hard():
    global PART, cache, distances
    PART = 2
    cache = {}
    for n, j in enumerate(imaginaries):
        for k, v in list(distances.items()):
            if 0 not in k:
                continue
            k = k[0] if k[1] == 0 else k[1]
            v -= 2
            d = inf
            if n == quadrant(k):
                d = v
            distances[(j, k)] = distances[(k, j)] = d
    distances = {k: v for k, v in distances.items() if 0 not in k}
    shortest(Letter.items[0])


DIR = pathlib.Path(__file__).parent.absolute()
inf = float("inf")
replacements = {".": 0, "#": -1, "@": -2}
for i, a in enumerate(ascii_lowercase):
    replacements[a] = i + 1
    replacements[a.upper()] = i + 101
rev_replacements = {v: k for k, v in replacements.items()}
t = read()
N = t[t < 100].max()
M = (t.shape[0] - 1) // 2
directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]
Letter(0, None)
cache = {}
distances = {}
PART = 1
imaginaries = [0.1, 0.2, 0.3, 0.4]
for i in imaginaries:
    rev_replacements[i] = "@"

if __name__ == "__main__":
    easy()
    hard()
