import pathlib


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return s[0]


def calc_hash(string):
    import hashlib

    return hashlib.md5(string.encode("utf8")).hexdigest()


def calc_hash_num(num, hard):
    s = calc_hash(t + str(num))
    if not hard:
        return s
    for _ in range(2016):
        s = calc_hash(s)
    return s


def get_hash(hashes, num, hard):
    cache = hashes.get(num)
    if cache is not None:
        return cache
    cache = calc_hash_num(num, hard)
    hashes[num] = cache
    return cache


def get_triplet(string):
    last = counter = 0
    for c in string:
        if last == c:
            counter += 1
            if counter >= 2:
                return [c]
        else:
            counter = 0
        last = c
    return []


def run(hard=False):
    hashes = {}
    i = found = 0
    while found < 64:
        for triplet in get_triplet(get_hash(hashes, i, hard)):
            for j in range(1000):
                if triplet * 5 in get_hash(hashes, i + j + 1, hard):
                    found += 1
                    if found == 64:
                        print(i)
                    break
        i += 1


def easy():
    run()


def hard():
    run(1)


teststr = ""  # "abc"
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
