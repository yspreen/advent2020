import pathlib


class State:
    def __init__(self, dmg2=None, hp1=50, hp2=None, mana=500):
        self.dmg2 = t[1] if dmg2 is None else dmg2
        self.hp1 = hp1
        self.hp2 = t[0] if hp2 is None else hp2
        self.mana = mana
        self.time_mana = 0
        self.amount_mana = 101
        self.time_armor = 0
        self.amount_armor = 7
        self.time_poi = 0
        self.amount_poi = 3
        self.mana_used = 0

    def clone(self):
        s = State()
        s.dmg2 = self.dmg2
        s.hp1 = self.hp1
        s.hp2 = self.hp2
        s.mana = self.mana
        s.time_mana = self.time_mana
        s.amount_mana = self.amount_mana
        s.time_armor = self.time_armor
        s.amount_armor = self.amount_armor
        s.time_poi = self.time_poi
        s.amount_poi = self.amount_poi
        s.mana_used = self.mana_used
        return s

    def step(self):
        if self.time_mana > 0:
            self.time_mana -= 1
            self.mana += self.amount_mana
        if self.time_armor > 0:
            self.time_armor -= 1
        if self.time_poi > 0:
            self.time_poi -= 1
            self.hp2 -= self.amount_poi
            if self.hp2 <= 0:
                return True

    @property
    def armor(self):
        return self.amount_armor if self.time_armor > 0 else 0

    def action(self, type, hard=0):
        if hard:
            self.hp1 -= 1
            if self.hp1 <= 0:
                return False
        s = self.step()
        if s is not None:
            return s
        if type == 0:
            self.mana -= 53
            self.mana_used += 53
            self.hp2 -= 4
        if type == 1:
            self.mana -= 73
            self.mana_used += 73
            self.hp1 += 2
            self.hp2 -= 2
        if type == 2:
            self.mana -= 113
            self.mana_used += 113
            self.time_armor = 6
        if type == 3:
            self.mana -= 173
            self.mana_used += 173
            self.time_poi = 6
        if type == 4:
            self.mana -= 229
            self.mana_used += 229
            self.time_mana = 5
        if self.mana < 0:
            return False
        if self.hp2 <= 0:
            return True
        s = self.step()
        if s is not None:
            return s
        self.hp1 -= max(self.dmg2 - self.armor, 1)
        if self.hp1 <= 0:
            return False


def read():
    with open(DIR / "input") as f:
        s = (f.read() if teststr == "" else teststr).splitlines()
    return lmap(lambda r: int(r.split(" ")[-1]), s)


def run(hard=0):
    pos, m = [State()], 9e9
    while pos:
        new = []
        for original in pos:
            for i in range(5):
                p = original.clone()
                won = p.action(i, hard=hard)
                if won is None:
                    new.append(p)
                elif won:
                    m = min(m, p.mana_used)
        pos = new
        if m != 9e9:
            return print(m)


def easy():
    run()


def hard():
    run(hard=1)


teststr = """"""
DIR = pathlib.Path(__file__).parent.absolute()
lmap = lambda *a: list(map(*a))
t = read()
if __name__ == "__main__":
    easy()
    hard()
