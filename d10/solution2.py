
map = []
with open("input.txt", "r") as file:

    for line in file:
        line = line[:-1]

        line = [int(item) for item in line]

        map.append(line)

res = 0

def bfs(i,j):

    h = map[i][j]

    if h == 9:
        global res
        res+=1
        return

    if i > 0 and map[i-1][j] == h + 1:
        bfs(i-1,j)

    if j > 0 and map[i][j-1] == h + 1:
        bfs(i,j-1)

    if i < len(map)-1 and map[i+1][j] == h + 1:
        bfs(i+1,j)
    
    if j < len(map)-1 and map[i][j+1] == h + 1:
        bfs(i,j+1)



for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            bfs(i,j)


print(res)