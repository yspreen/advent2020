input = [
'78, 335',
'74, 309',
'277, 44',
'178, 286',
'239, 252',
'118, 354',
'170, 152',
'75, 317',
'156, 318',
'172, 45',
'138, 162',
'261, 195',
'306, 102',
'282, 67',
'53, 141',
'191, 237',
'352, 180',
'95, 247',
'353, 357',
'201, 327',
'316, 336',
'57, 43',
'119, 288',
'299, 328',
'125, 327',
'187, 186',
'121, 151',
'121, 201',
'43, 67',
'76, 166',
'238, 148',
'326, 221',
'219, 207',
'237, 160',
'345, 244',
'321, 346',
'48, 114',
'304, 80',
'265, 216',
'191, 92',
'54, 75',
'118, 260',
'336, 249',
'81, 103',
'290, 215',
'300, 246',
'293, 59',
'150, 274',
'296, 311',
'264, 286',
]

maxd = 10000

input = [[int(i.split(', ')[0]), int(i.split(', ')[1])] for i in input]
min_x = min([i[0] for i in input])
min_y = min([i[1] for i in input])

for i in input:
    i[0] -= min_x
    i[1] -= min_y

max_x = max([i[0] for i in input]) + 1
max_y = max([i[1] for i in input]) + 1

def main():
    global input
    from contextlib import suppress

    arr = [([[-1, max_x + max_y] for _ in range(max_y)] + [0]) for _ in range(max_x)] + [([0 for _ in range(max_y)] + [0])]

    c = 0
    for x in range(max_x):
        for y in range(max_y):
            d = 0
            for i in input:
                d += abs(i[0] - x)
                d += abs(i[1] - y)
                if d > maxd:
                    break
            if d < maxd:
                c += 1
    print(c)
main()
