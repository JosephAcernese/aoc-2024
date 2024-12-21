
map = []
with open("input.txt", "r") as file:

    for line in file:
        line = line[:-1]

        line = [int(item) for item in line]

        map.append(line)

res = {}

def bfs(i,j,k,l):

    h = map[i][j]

    if h == 9:

        if (k,l) not in res:
            res[(k,l)] = [(i,j)]
        elif (i,j) not in res[(k,l)]:
            res[(k,l)].append((i,j))

        return

    if i > 0 and map[i-1][j] == h + 1:
        bfs(i-1,j,k,l)

    if j > 0 and map[i][j-1] == h + 1:
        bfs(i,j-1,k,l)

    if i < len(map)-1 and map[i+1][j] == h + 1:
        bfs(i+1,j,k,l)
    
    if j < len(map)-1 and map[i][j+1] == h + 1:
        bfs(i,j+1,k,l)



for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            bfs(i,j,i,j)

sum = 0
for k in res:
    sum += len(res[k])

print(sum)