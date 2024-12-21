nums = list([2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0])


def calc(A, nums):
    try:
        return (((A % 8) ^ nums[3]) ^ nums[7]) ^ (A // 2 ** ((A % 8) ^ nums[3])) % 8
    except Exception:
        return


def find_number(i=0, prev=0):
    if i == len(nums):
        return prev // 8
    for A in range(prev, prev + 8):
        if calc(A, nums) != nums[-i - 1]:
            continue
        future = find_number(i + 1, prev=A * 8)
        if future is not None:
            return future

    return None


print(find_number())
