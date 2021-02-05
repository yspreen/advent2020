serial = 7139
serial %= 1000

def main():
    global serial
    
    arr = [[0 for _ in range(300)] for _ in range(300)]

    rack = 10
    for x in range(300):
        rack += 1
        level = 0
        for y in range(300):
            level += rack
            arr[x][y] = (rack * (level + serial)) // 100 % 10 - 5
    
    sums = {}
    for size in range(10, 21):
        for x in range(300 - size + 1):
            for y in range(300 - size + 1):
                s = 0
                for col in arr[x:(x+size)]:
                    for el in col[y:(y+size)]:
                        s += el
                sums["%d,%d,%d" % (x+1,y+1,size)] = s
    max = 0
    max_ind = 0
    for ind in sums:
        if sums[ind] > max:
            max = sums[ind]
            max_ind = ind
    print(max, max_ind)
main()
