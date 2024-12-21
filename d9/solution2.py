input = ""
with open("input.txt", "r") as file:

    for line in file:
        line= line[:-1]
        input+= line


class File():
    def __init__(self,id,space):
        self.id = id
        self.space = space

    def copy(self):
        return File(self.id,self.space)

mem = []
used = True
id = 0

for c in input:
    c = int(c)
    if used:
        mem.append(File(id,c))
        id+=1
        used = False

    else:
        mem.append(File(-1,c))
        used = True

l = 0
r = len(mem)-1

while l < r:

    if mem[l].id != -1:
        l+=1
        continue
    elif mem[r].id == -1:
        r-=1
        continue

    l2 = l

    while l2 < r:

        if mem[l2].space < mem[r].space or mem[l2].id != -1:
            l2+=1

        elif mem[l2].space == mem[r].space:
            mem[l2].id = mem[r].id
            mem[r].id = -1
            break

        else:

            mem[l2].space -= mem[r].space
            mem.insert(l2, File(mem[r].id,mem[r].space))
            mem[r].id = -1

            break

    r-=1


ptr = 0
res = 0
seen = set() # There is a weird bug where sometimes when files are moved the original is not deleted, this is the perfect bandaid

for file in mem:



    if file.id == -1:
        ptr += file.space
    
    elif file.id not in seen:
        for i in range(file.space):
            res += file.id * ptr
            ptr += 1
        seen.add(file.id)

print(res)