import math
map = []
with open("input.txt", "r") as file:

    for line in file:
        line= line[:-1]
        map.append(line)

antinodes = set()
antennas = {}


for i in range(len(map)):
    for j in range(len(map[0])):
        c = map[i][j]
        if c != ".":
            if c in antennas:
                antennas[c].append((i,j))
            else:
                antennas[c] = [(i,j)]


for key in antennas:
    p = antennas[key]
    for p1 in p:
        for p2 in p:

            if p1 == p2:
                antinodes.add(p1)
                continue

            line = (p1[0] - p2[0], p1[1] - p2[1])
            anti = (p1[0] + line[0], p1[1] + line[1])

            while anti[0] >= 0 and anti[1] >= 0 and anti[0] < len(map) and anti[1] < len(map[0]):

                antinodes.add(anti)
                anti = (anti[0] + line[0], anti[1] + line[1])



print(len(antinodes))