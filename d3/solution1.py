import re

code = ""

with open("input.txt", "r") as file:
    for line in file:
        code+=line


pattern = "mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, code)
res = 0

for t in matches:
    res += int(t[0]) * int(t[1])

print(res)

    