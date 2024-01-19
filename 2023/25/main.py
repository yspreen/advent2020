import pathlib
from os import environ
from collections import deque


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).replace(":", "").splitlines()
    s = lmap(lambda r: r.split(" "), s)
    keys = list(set(i for r in s for i in r))
    graph = [[0 for _ in keys] for _ in keys]
    for row in s:
        first, others = row[0], row[1:]
        for other in others:
            graph[keys.index(first)][keys.index(other)] = 1
            graph[keys.index(other)][keys.index(first)] = 1
    return graph, keys


def bfs(rGraph, s, t, parent):
    visited = [False] * len(rGraph)
    queue = deque([s])
    visited[s] = True

    while queue:
        u = queue.popleft()

        for ind, val in enumerate(rGraph[u]):
            if visited[ind] is False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[t]


def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    rGraph = [row[:] for row in graph]

    while bfs(rGraph, source, sink, parent):
        path_flow = float("inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, rGraph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]

    return max_flow, rGraph


def find_min_cut_edges(graph, rGraph, source):
    visited = [False] * len(rGraph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for ind, val in enumerate(rGraph[u]):
            if visited[ind] is False and val > 0:
                queue.append(ind)
                visited[ind] = True

    min_cut_edges = []
    for i in range(len(rGraph)):
        for j in range(len(rGraph[i])):
            if rGraph[i][j] == 0 and graph[i][j] > 0 and visited[i] and not visited[j]:
                min_cut_edges.append((i, j))

    sub_l = {i for i, val in enumerate(visited) if val}
    sub_r = set(range(len(graph))) - sub_l

    return min_cut_edges, (sub_l, sub_r)


def global_min_cut(graph):
    min_cut_value = float("inf")
    min_cut_edges = []
    graphs = ([], [])

    for source in range(len(graph)):
        for sink in range(len(graph)):
            if source != sink:
                cut_value, rGraph = edmonds_karp(graph, source, sink)
                if cut_value < min_cut_value:
                    min_cut_value = cut_value
                    min_cut_edges, graphs = find_min_cut_edges(graph, rGraph, source)
                if cut_value == 3:
                    return min_cut_value, min_cut_edges, graphs

    # return min_cut_value, min_cut_edges, graphs


def easy():
    # for a, b in global_min_cut(t)[1]:
    #     print(u[a], u[b])
    graphs = global_min_cut(t)[2]
    print(len(graphs[0]) * len(graphs[1]))


def hard():
    return


teststr = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""
if environ.get("AOC_SOLVE", "") == "1":
    teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
inf = float("inf")
t, u = read()
if __name__ == "__main__":
    easy()
    hard()
