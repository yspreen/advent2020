input = "400 players; last marble is worth 71864 points"
input = [int(input.split(" ")[0]), int(input.split(" ")[-2])]

def insert(arr, ind, num):
    return arr[:ind] + [num] + arr[ind:]
def remove(arr, ind):
    v = arr[ind]
    del arr[ind]
    return v

def main():
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
            scores[player] += remove(marbles, current)
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


main()
