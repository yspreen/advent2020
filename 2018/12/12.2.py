input = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
"""
input = """
initial state: ##..#.#.#..##..#..##..##..#.#....#.....##.#########...#.#..#..#....#.###.###....#..........###.#.#..

..##. => .
..... => .
##..# => .
...#. => .
#.... => .
...## => #
.#.#. => .
#..#. => #
##.#. => .
#..## => .
..#.. => .
#.#.# => .
###.# => .
###.. => .
.#... => #
.##.# => .
##... => #
..### => .
####. => .
#...# => #
.#..# => #
##### => #
..#.# => #
.#.## => #
#.### => .
....# => .
.###. => .
.#### => #
.##.. => .
##.## => #
#.##. => #
#.#.. => #
"""

input = input.split("\n")
input = list(filter(None, input))

state = input[0].split(" ")[-1]
input = input[1:]
rules = {i.split(" ")[0]: i.split(" ")[-1] for i in input}
rule_len = 0
for r in rules:
    rule_len = len(r)
    break

def main():
    global rules, state, rule_len
    rule_len_side = rule_len // 2
    prefix = "".join(["." for _ in range(rule_len_side)])
    shift = 0
    iterations = 1500
    last_s = 0
    
    for i in range(iterations):
        new_state = ""

        if state[0] == '#':
            state = prefix + state
            shift += 2
        if state[-1] == '#':
            state = state + prefix
        state = prefix + state + prefix
        while len(state) >= rule_len:
            new_state += rules.get(state[0:rule_len], ".")
            state = state[1:]

        state = new_state
        if i > 1000:
            if i > 1100:
                break
            s = 0
            for j in range(len(state)):
                if state[j] == '#':
                    s += j - shift
            print(i+1, s, s - last_s)
            last_s = s
    print((50000000000 - i) * 23 + last_s)

    
main()
