from llist import sllist

input = 190221

def main():
    global input
    
    recipes = sllist([3,7])
    first_elf = recipes.first
    second_elf = recipes.first.next
    num_recipes = len(recipes)

    while num_recipes < input + 10:
        s = first_elf.value + second_elf.value
        for r in str(s):
            r = int(r)
            recipes.appendright(r)
            num_recipes += 1
        for _ in range(first_elf.value + 1):
            first_elf = first_elf.next
            if first_elf is None:
                first_elf = recipes.first
        for _ in range(second_elf.value + 1):
            second_elf = second_elf.next
            if second_elf is None:
                second_elf = recipes.first
    for _ in range(input):
        recipes.popleft()
    print("".join([str(r) for r in recipes])[:10])
main()
