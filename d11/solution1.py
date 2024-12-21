stones = None

with open("input2.txt", "r") as file:

    for line in file:
        line = line[:-1].split(" ")

        stones = line


def magicTrick(stone):

    if stone == "0":
        return ["1"]

    elif len(stone) % 2 == 0:

        l = int(stone[len(stone)//2:])
        r = int(stone[ :len(stone) // 2 ])
        return [str(l), str(r)]

    else:
        return [str(int(stone) * 2024)]


count = 0 

while count < 25:

    i = 0
    while i < len(stones):

        new = magicTrick(stones.pop(i))
        
        for s in new:
            stones.insert(i,s)

        i+=len(new)

        
    count+=1

print(len(stones))

        
        