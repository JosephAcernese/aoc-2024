map = []

with open("input.txt", "r") as file:

    for line in file:
        line = line[:-1]

        map.append(list(line))


visited = set()

def dfs(i,j,area = 0, perimeter = 0):

    if (i,j) in visited:
        return (0,0)

    visited.add((i,j))
    area+=1

    if i == 0 or map[i-1][j] != map[i][j]:
        perimeter += 1

    else:
        temp = dfs(i-1,j)
        area += temp[0]
        perimeter += temp[1]

    if i == len(map)-1 or map[i+1][j] != map[i][j]:
        perimeter+=1

    else:
        temp = dfs(i+1,j)
        area += temp[0]
        perimeter += temp[1]   
        
    if j == 0 or map[i][j-1] != map[i][j]:
        perimeter += 1

    else:
        temp = dfs(i,j-1)
        area += temp[0]
        perimeter += temp[1]

    if j == len(map[0])-1 or map[i][j+1] != map[i][j]:
        perimeter+=1

    else:
        temp = dfs(i,j+1)
        area += temp[0]
        perimeter += temp[1]

    return (area,perimeter)

def countSides(visited):

    i = float("inf")
    j = float("inf")
    for pos in visited:
        if pos[0] < i:
            i = pos[0]

    for pos in visited:
        if pos[0] == i and pos[1] < j:
            j = pos[1]

    sides = 0
    start = (i,j)

    dir = ""

    while sides == 0 or ((i,j) != start and dir != "l"):



res = 0

for i in range(len(map)):
    for j in range(len(map[0])):
        if (i,j) not in visited:
            visited = set()
            x = dfs(i,j)
            res += x[0] * x[1]


print(res)

    
    