input = ""
with open("input.txt", "r") as file:

    for line in file:
        line= line[:-1]
        input+= line

mem = []
used = True
id = 0

for c in input:

    if used:
        for i in range(int(c)):
            mem.append(id)
        id+=1
        used = False

    else:
        for i in range(int(c)):
            mem.append(".")
        used = True

l = 0
r = len(mem)-1

while l < r:
    if mem[l] != ".":
        l+=1 
    
    elif mem[r] == ".":
        r -= 1
        mem.pop()

    else:

        mem[l] = mem[r]
        mem.pop()
        r-=1
        l+=1
    
res = 0

for i in range(len(mem)):
    if mem[i] == ".":
        break
    res += mem[i] * i

print(res)