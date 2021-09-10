import pathlib


def lmap(*a):
    return list(map(*a))


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    s_ = []
    for l in lmap(lambda r: lmap(str, r.replace("output ", "output -1").split(" ")), s):
        if l[0] == "bot":
            s_.append(tuple(map(int, [l[1], l[6], l[11]])))
        else:
            s_.append(tuple(map(int, [l[1], l[5]])))
    return s_


class Bot:
    items = {}

    def __init__(self, num):
        self.num = num
        self.val = []

    @classmethod
    def get(cls, num):
        cls.items[num] = cls.items.get(num, Bot(num))
        return cls.items[num]

    def add(self, num):
        if len(self.val) < 2:
            self.val.append(num)

    @property
    def full(self):
        return len(self.val) == 2

    def give(self, min_bot, max_bot):
        min_bot.add(min(self.val))
        max_bot.add(max(self.val))
        if 61 in self.val and 17 in self.val:
            print(self.num)
        self.val = []


def output(num):
    return Bot.get(int("-1" + str(num))).val[0]


def easy():
    done = set()
    while len(done) != len(t):
        for ins in set(t) - done:
            if len(ins) == 2:
                bot = Bot.get(ins[1])
                bot.add(ins[0])
                done.add(ins)
                continue
            bot1 = Bot.get(ins[0])
            bot2 = Bot.get(ins[1])
            bot3 = Bot.get(ins[2])
            if not bot1.full:
                continue
            if bot2.full or bot3.full:
                continue
            bot1.give(bot2, bot3)
            done.add(ins)
    print(output(0) * output(1) * output(2))


def hard():
    return


teststr, _ = (
    "",
    """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2""",
)
DIR = pathlib.Path(__file__).parent.absolute()
t = read()
if __name__ == "__main__":
    easy()
    hard()
