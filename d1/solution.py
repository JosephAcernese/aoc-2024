import numpy as np


left_numbers = []
right_numbers = []

# Read the file
with open("input.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_numbers.append(left)
        right_numbers.append(right)

left_numbers.sort()
right_numbers.sort()

dict = {}
res = 0

for n in right_numbers:
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1

for n in left_numbers:

    if n not in dict:
        continue
    res += dict[n] * n
    
    
print(res)

