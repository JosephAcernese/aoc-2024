from copy import deepcopy

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

def isInfinite(i,j,new_i,new_j,board):

    dict = {}

    board[new_i][new_j] = "#"

    while True:

        if (i,j) in dict:
            if board[i][j] in dict[(i,j)]:
                return True

            else:
                dict[(i,j)].append(board[i][j])

        else:
            dict[(i,j)] = [board[i][j]]


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
            return False

        while board[dir[0] + i][dir[1] + j] == "#":
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

        board[next_i][next_j] = board[i][j]
        board[i][j] = "."
        i = next_i
        j = next_j

res = 0
for k in range(len(board)):
    for l in range(len(board[0])):
        if board[k][l] == ".":
            if isInfinite(i,j,k,l,deepcopy(board)):
                res+=1

print(res)
