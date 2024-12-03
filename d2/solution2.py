import numpy as np


reports = []

# Read the file
with open("input.txt", "r") as file:
    for line in file:
        nums = line.split()
        nums = list(map(int, nums))
        reports.append(nums)


res = 0

def isSafe(r):

    if r[0] < r[1]:
        increasing = True

    else:
        increasing = False


    for i in range(len(r)-1):

        if r[i] < r[i+1] and not increasing:
            return False

        if r[i] > r[i+1] and increasing:
            return False

        if r[i] == r[i+1]:
            return False

        diff = r[i] - r[i+1]

        if diff < -3 or diff > 3:
            return False

    return True

for r in reports:

    if isSafe(r):
        res+=1
    
    else:
        for i in range(len(r)):
            r2 = r[0:i] + r[i+1:len(r)]
            if isSafe(r2):
                res+=1
                break

print(res)

        


        
        