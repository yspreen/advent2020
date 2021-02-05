from llist import sllist

input = 190221

def main():
    global input
    
    input = str(input)
    recipes = sllist([3,7])
    recent_recipes = sllist([])
    recent_len = 0
    input_len = len(input)
    first_elf = recipes.first
    second_elf = recipes.first.next
    num_recipes = len(recipes)
    is_done = False
    input = sllist([int(i) for i in input])

    while not is_done:
        s = first_elf.value + second_elf.value
        for r in str(s):
            r = int(r)
            recipes.appendright(r)
            num_recipes += 1
            recent_recipes.appendright(r)
            if recent_len == input_len:
                recent_recipes.popleft()
            else:
                recent_len += 1
            if recent_recipes == input:
                is_done = True
                break
        for _ in range(first_elf.value + 1):
            first_elf = first_elf.next
            if first_elf is None:
                first_elf = recipes.first
        for _ in range(second_elf.value + 1):
            second_elf = second_elf.next
            if second_elf is None:
                second_elf = recipes.first
    print(num_recipes - len(input))
main()
