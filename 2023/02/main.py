with open("input") as f:
    text = f.read()

maximums = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

sum_of_ids = 0
for line in text.splitlines():
    game_id = line.split(":")[0].split(" ")[1]
    draws = line.split(": ")[1]
    is_possible = True
    for draw in draws.split("; "):
        for color in draw.split(", "):
            color_name = color.split(" ")[1]
            number = int(color.split(" ")[0])

            if number > maximums[color_name]:
                is_possible = False
    if is_possible:
        sum_of_ids += int(game_id)

print(sum_of_ids)

sum_of_powers = 0
for line in text.splitlines():
    game_id = line.split(":")[0].split(" ")[1]
    draws = line.split(": ")[1]
    minimums = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for draw in draws.split("; "):
        for color in draw.split(", "):
            color_name = color.split(" ")[1]
            number = int(color.split(" ")[0])

            minimums[color_name] = max(minimums[color_name], number)
    sum_of_powers += minimums["red"] * minimums["green"] * minimums["blue"]

print(sum_of_powers)
