from random import choice
from sys import argv

i = ""

for j in argv[1:]:
    i += j + " "

r = ""

for _ in range(5):
    for t in i:
        if choice([True, False]):
            r += t.upper()
        else:
            r += t.lower()
    r += "\n"

print(r[:-1])