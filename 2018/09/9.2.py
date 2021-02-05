from llist import dllist as llist

input = "400 players; last marble is worth 71864 points"
input = [int(input.split(" ")[0]), int(input.split(" ")[-2])]
input[1] *= 100

def remove(lst, ind):
    node = lst.nodeat(ind)
    lst.remove(node)
    return node.value

def main():
    global input
    from datetime import datetime
    
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


main()
