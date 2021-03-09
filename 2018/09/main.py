import pathlib

input = open(pathlib.Path(__file__).parent / "input").read().splitlines()[0]
input = [int(input.split(" ")[0]), int(input.split(" ")[-2])]


def insert(arr, ind, num):
    return arr[:ind] + [num] + arr[ind:]


def remove_easy(arr, ind):
    v = arr[ind]
    del arr[ind]
    return v


def easy():
    global input

    marbles = [0]
    marble = 1
    player = 0
    scores = [0 for _ in range(input[0])]
    current = 0
    while True:
        # print("".join([("(" + str(m) + ")") if marbles[current] == m else " " + str(m) + " " for m in marbles]))
        if marble % 23 == 0:
            scores[player] += marble
            current += len(marbles) - 7
            current %= len(marbles)
            scores[player] += remove_easy(marbles, current)
        else:
            current += 2
            current %= len(marbles)
            marbles = insert(marbles, current, marble)
            # if current == 0 and len(marbles) == 2:
            #     marbles = [marbles[-1]] + marbles[:-1]
            #     current += 1
            # if current == 0 and len(marbles) != 2:
            #     marbles = marbles[1:] + [marbles[0]]
            #     current -= 1
        if marble == input[1]:
            break
        marble += 1
        player += 1
        player %= input[0]
    print(max(scores))


easy()
input[1] *= 100


def remove(lst, ind):
    node = lst.nodeat(ind)
    lst.remove(node)
    return node.value


def hard():
    global input
    from datetime import datetime
    from llist import dllist as llist

    marbles = llist([0])

    marble = 1
    player = 0
    scores = [0 for _ in range(input[0])]
    time = datetime.now()
    beginning = marbles
    end = marbles.nodeat(0)
    cursor = marbles.first
    while True:
        # print("".join([("(" + str(m) + ")") if cursor.value == m else " " + str(m) + " " for m in marbles]))
        if marble % 23 == 0:
            scores[player] += marble
            for _ in range(7):
                if cursor.prev is None:
                    cursor = marbles.last
                else:
                    cursor = cursor.prev
            scores[player] += cursor.value
            if cursor.next is None:
                marbles.remove(cursor)
                cursor = marbles.last
            else:
                cursor = cursor.next
                marbles.remove(cursor.prev)
        else:
            for _ in range(2):
                if cursor.next is None:
                    cursor = marbles.first
                else:
                    cursor = cursor.next
            marbles.insert(marble, cursor)
            cursor = cursor.prev
        if marble == input[1]:
            break
        marble += 1
        player += 1
        if player >= input[0]:
            player -= input[0]
    print(max(scores))


hard()
