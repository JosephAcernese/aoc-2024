from functools import cache 

stones = None

with open("input.txt", "r") as file:

    for line in file:
        line = line[:-1].split(" ")

        stones = line

@cache
def magicTrick(stone,t):

    if t == 0:
        return 1

    if stone == "0":
        return magicTrick("1",t-1)

    elif len(stone) % 2 == 0:

        l = int(stone[len(stone)//2:])
        r = int(stone[ :len(stone) // 2 ])
        return magicTrick(str(l),t-1) + magicTrick(str(r),t-1)

    else:
        return magicTrick(str(int(stone) * 2024),t-1)


count = 0 
res = 0

for stone in stones:
    res+=magicTrick(stone,75)

print(res)

        
        