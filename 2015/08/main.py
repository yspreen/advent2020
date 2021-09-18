import re
import pathlib
import codecs


def read():
    with open(DIR / "input") as f:
        s, e = (f.read() if teststr == "" else teststr).splitlines(), "unicode_escape"
    for i, v in enumerate(s):
        s[i] = (v, codecs.decode(re.sub(r'\\x[^"]{2}', "\\\\x61", v)[1:-1], e))
    return len("".join(map(lambda i: i[0], s))), s


teststr = """\"\"
"abc"
"aaa\\"aaa"
"\\x27\""""
teststr = ""
DIR = pathlib.Path(__file__).parent.absolute()
N, t = read()
if __name__ == "__main__":
    print(N - len("".join(map(lambda i: i[1], t))))
    print(sum(map(lambda i: 2 + i[0].count('"') + i[0].count("\\"), t)))
