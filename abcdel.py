from sys import argv

l = ["a", "e", "i", "o", "u"]
t = ""

for i in argv[1:]:
    t += i + " "

r = ""

for i in t:
    if i not in l:
        r += i

print(r)