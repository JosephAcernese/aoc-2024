import numpy as np


reports = []

# Read the file
with open("input.txt", "r") as file:
    for line in file:
        nums = line.split()
        nums = list(map(int, nums))
        reports.append(nums)


res = 0

for r in reports:

    if r[0] < r[1]:
        increasing = True

    else:
        increasing = False

    valid = True

    for i in range(len(r)-1):

        if r[i] < r[i+1] and not increasing:
            valid = False
            break

        if r[i] > r[i+1] and increasing:
            valid = False
            break

        if r[i] == r[i+1]:
            valid = False
            break

        diff = r[i] - r[i+1]

        if diff < -3 or diff > 3:
            valid = False
            break

    if valid:
        res+=1


print(res)

        


        
        