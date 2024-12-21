map = []
with open("input.txt", "r") as file:

    for line in file:
        line= line[:-1]
        map.append(line)

antinodes = {}
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
    for i in range(len(p)):
        for j in range(len(p)):

            if i == j:
                continue

            dis = (p[i][0] - p[j][0], p[i][1] - p[j][1])
            anti_pos = (p[i][0] + dis[0], p[i][1] + dis[1])

            if anti_pos[0] < 0 or anti_pos[1] < 0 or anti_pos[0] >= len(map) or anti_pos[1] >= len(map[0]):
                continue

            if not anti_pos in antinodes:
                antinodes[anti_pos] = 1


print(len(antinodes))