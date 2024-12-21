

rules = {}
updates = []

with open("input.txt", "r") as file:

    rule = True
    for line in file:
        line = line[:-1]

        if line == "":
            rule = False
            continue

        if rule:        
            temp = line.split("|")
            temp = [int(temp[0]),int(temp[1])]

            if temp[1] in rules:
                rules[temp[1]].append(temp[0])
            
            else:
                rules[temp[1]] = [temp[0]]

        else:
            temp = line.split(",")
            temp = list(map(int, temp))
            updates.append(temp)


    res = 0 

    for u in updates:
        disallowed = []
        valid = True

        for p in u:

            if p in disallowed:
                valid = False
                break

            else:
                disallowed += rules[p]

        if valid:
            res += u[len(u)//2]

    print(res)
