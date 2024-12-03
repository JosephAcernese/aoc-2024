import re

code = ""

with open("input.txt", "r") as file:
    for line in file:
        code+=line


pattern ="mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)"

matches = re.findall(pattern, code)
res = 0
do = True

for t in matches:

    if t[3] == "don't":
        do = False

    elif t[2] == "do":
        do = True

    elif do:
        res += int(t[0]) * int(t[1])

print(res)

    