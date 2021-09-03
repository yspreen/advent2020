import re
import pathlib

DIR = pathlib.Path(__file__).parent.absolute()


class Rule:
    unresolved = set()
    rules = {}

    def __init__(self, s):
        self.id = int(s.split(":")[0])
        Rule.rules[self.id] = self
        Rule.unresolved.add(self)
        self.raw = s.split(":")[1]
        self.resolved = False
        self.children = set()
        for token in self.raw.split(" "):
            try:
                self.children.add(int(token))
            except:
                pass

    def resolve(self, advanced=False):
        if self.resolved:
            return
        if len(self.children) == 0:
            self.parsed = self.raw.replace('"', "")[1:]
            self.resolved = True
            Rule.unresolved.discard(self)
            return
        parsed = self.raw
        # Sort to avoid shorter substrings
        for c in sorted(list(self.children), reverse=True):
            c = Rule.rules[c]
            if not c.resolved:
                return
            parsed = parsed.replace(" %d" % c.id, c.parsed)
        if advanced and self.id == 8:
            self.parsed = "%s+" % Rule.rules[42].parsed
        elif advanced and self.id == 11:
            parsed = "("
            for i in range(1, 6):  # max 5 recursions
                parsed += "%s{%d}%s{%d}|" % (
                    Rule.rules[42].parsed,
                    i,
                    Rule.rules[31].parsed,
                    i,
                )
            self.parsed = parsed[:-1] + ")"
        else:
            self.parsed = "(%s)" % parsed.replace(" |", "|")

        self.resolved = True
        Rule.unresolved.discard(self)


def read(advanced=False):
    with open(DIR / "input") as f:
        t = f.read().replace("\r", "").split("\n\n")

    rules = t[0].split("\n")
    lines = t[1].split("\n")
    if lines[-1] == "":
        lines.pop()
    for r in rules:
        Rule(r)
    while len(Rule.unresolved):
        for r in Rule.rules.values():
            r.resolve(advanced=advanced)
    return lines


def match(lines):
    regex = Rule.rules[0].parsed
    match = 0
    for line in lines:
        if re.match("^%s$" % regex, line):
            match += 1
    print(match)


def easy():
    match(read())


def hard():
    match(read(True))


if __name__ == "__main__":
    easy()
    hard()
