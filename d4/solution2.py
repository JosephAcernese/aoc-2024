

search = []

with open("input.txt", "r") as file:

    for line in file:
        line = line[:-1]
        search.append(line)
    
res = 0

for i in range(len(search)):
    for j in range(len(search[0])):

        if search[i][j] == "M" and i+2 < len(search) and j+2 < len(search[0]):
            if search[i+2][j] == "M" and search[i+1][j+1] == "A" and search[i+2][j+2] == "S" and search[i][j+2] == "S":
                res+=1
            if search[i+2][j] == "S" and search[i+1][j+1] == "A" and search[i+2][j+2] == "S" and search[i][j+2] == "M":
                res+=1

        if search[i][j] == "S" and i+2 < len(search) and j+2 < len(search[0]):
            if search[i+2][j] == "S" and search[i+1][j+1] == "A" and search[i+2][j+2] == "M" and search[i][j+2] == "M":
                res+=1
            if search[i+2][j] == "M" and search[i+1][j+1] == "A" and search[i+2][j+2] == "M" and search[i][j+2] == "S":
                res+=1

print(res)

