import pathlib

input = open(pathlib.Path(__file__).parent / "input").read().splitlines()
chars = {
    ".": 0,
    "#": 1,
    "E": 2,
    "G": 3,
}


units = arr = dim_x = dim_y = max_val = 0


def read():
    global units, arr, dim_y, dim_x, max_val
    units = []
    arr = [[0 for _ in input] for _ in input[0]]
    dim_x = len(arr)
    dim_y = len(arr[0])
    max_val = dim_x * dim_y
    for y in range(dim_y):
        for x in range(dim_x):
            c = input[y][x]
            c = chars[c]
            if c > 1:
                units.append([c, [x, y], 200, 3])
            arr[x][y] = c


def sort_units():
    global units, dim_x
    units = sorted(units, key=lambda u: u[1][1] * dim_x + u[1][0])


def neighbors(x):
    global dim_x, dim_y
    y = x[1]
    x = x[0]
    n = []
    if y > 0:
        n.append((x, y - 1))
    if x > 0:
        n.append((x - 1, y))
    if x < dim_x - 1:
        n.append((x + 1, y))
    if y < dim_y - 1:
        n.append((x, y + 1))
    return n


def fight(u, e):
    global units
    killed = 0
    for i in range(len(units)):
        if units[i][1][0] == e[1][0] and units[i][1][1] == e[1][1]:
            e[2] -= u[3]
            if e[2] <= 0:
                arr[e[1][0]][e[1][1]] = 0
                killed = e[0]
                del units[i]
            return killed
    print("no fight!")


def enemies(u):
    global units
    e = []
    for unit in units:
        if unit[0] > 1 and unit[0] != u[0]:
            e.append(unit)
    return e


def get_distances(point):
    global arr, dim_x, dim_y, max_val
    d = [[-1 for _ in arr[0]] for _ in arr]
    d[point[0]][point[1]] = 0
    goals = [point]
    while len(goals):
        new_goals = []
        for goal in goals:
            for (x, y) in neighbors(goal):
                if arr[x][y] != 0:
                    continue
                if d[x][y] == -1:
                    new_goals.append((x, y))
                    d[x][y] = max_val
                d[x][y] = min([d[x][y], d[goal[0]][goal[1]] + 1])
        goals = new_goals
    return d


def move_to(unit, goal):
    global arr
    distances = get_distances(goal)
    min_d = (max_val, 0)
    for (x, y) in neighbors(unit[1]):
        d = distances[x][y]
        if d >= 0 and d < min_d[0]:
            min_d = (d, (x, y))
    goal = min_d[1]
    if goal == 0:
        print("invalid move")
    arr[unit[1][0]][unit[1][1]] = 0
    unit[1] = goal
    arr[unit[1][0]][unit[1][1]] = unit[0]


def attempt(power=3):
    global arr, max_val

    read()
    for u in units:
        if u[0] == 2:
            u[3] = power if power > 0 else u[3]
    rounds = 0
    while True:
        unitscopy = [u for u in units]
        for unit in unitscopy:
            if unit[2] <= 0:
                continue
            lowest = (0, 0, 10000, 0)
            for (x, y) in neighbors(unit[1]):
                c = arr[x][y]
                if c > 1:
                    if c != unit[0]:
                        e = None
                        for enemy in units:
                            if enemy[1][0] == x and enemy[1][1] == y:
                                e = enemy
                                break
                        if e[2] < lowest[2]:
                            lowest = e
            if lowest[0] > 1:
                if fight(unit, lowest) == 2 and power > 0:
                    # print("Someone died :(")
                    return False
            else:
                goals = []
                has_enemy = False
                for e in enemies(unit):
                    has_enemy = True
                    for (x, y) in neighbors(e[1]):
                        if arr[x][y] == 0:
                            goals.append((x, y))
                if not has_enemy:
                    s = 0
                    for unit in units:
                        s += unit[2]
                    print(s * rounds)
                    return True
                goals = sorted(goals, key=lambda g: g[1] * dim_x + g[0])
                distances = get_distances(unit[1])
                min_goal = (max_val, 0)
                for goal in goals:
                    d = distances[goal[0]][goal[1]]
                    if d > -1 and d < min_goal[0]:
                        min_goal = (d, goal)
                if min_goal[1] != 0:
                    move_to(unit, min_goal[1])
                    sort_units()
                lowest = (0, 0, 10000, 0)
                for (x, y) in neighbors(unit[1]):
                    c = arr[x][y]
                    if c > 1:
                        if c != unit[0]:
                            e = None
                            for enemy in units:
                                if enemy[1][0] == x and enemy[1][1] == y:
                                    e = enemy
                                    break
                            if e[2] < lowest[2]:
                                lowest = e
                if lowest[0] > 1:
                    if fight(unit, lowest) == 2 and power > 0:
                        # print("Someone died :(")
                        return False
        rounds += 1


attempt(-1)
for p in range(1, 30):
    if attempt(p):
        break
