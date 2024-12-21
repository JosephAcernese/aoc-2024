
board = []

with open("input.txt", "r") as file:

    for line in file:
        line = list(line[:-1])
        board.append(line)

i = -1
j = -1

for k in range(len(board)):
    for l in range(len(board[0])):
        if board[k][l] != "#" and board[k][l] != ".":
            i = k
            j = l
            break

res = 0


while True:

    if board[i][j] == ">":
        dir = [0,1]

    elif board[i][j] == "v":
        dir = [1,0]

    elif board[i][j] == "^":
        dir = [-1,0]

    elif board[i][j] == "<":
        dir = [0,-1]
 
    next_i,next_j = dir[0] + i, dir[1] + j

    if next_i < 0 or next_i >= len(board) or next_j < 0 or next_j >= len(board[0]):
        break

    while board[dir[0] + i][ dir[1] + j] == "#" or board[dir[0] + i][ dir[1] + j] == "O":
        if board[i][j] == ">":
            board[i][j] = "v"
            dir = [1,0]

        elif board[i][j] == "v":
            board[i][j] = "<"
            dir = [0,-1]
        
        elif board[i][j] == "<":
            board[i][j] = "^"
            dir = [-1,0]
    
        elif board[i][j] == "^":
            board[i][j] = ">"
            dir = [0,1]


    next_i,next_j = dir[0] + i, dir[1] + j

    if res == 0:
        res += 1

    if board[next_i][next_j] == ".":
        res+=1

    board[next_i][next_j] = board[i][j]
    board[i][j] = "X"
    i = next_i
    j = next_j


print(res)
