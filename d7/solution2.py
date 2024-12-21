
equations = []

with open("input.txt", "r") as file:

    for line in file:
        line = line.split(" ")
        line[0] = line[0][:-1]
        line[-1] = line[-1][:-1]

        line = [int(item) for item in line]

        equations.append(line)

res = 0

def calculateFunction(final,numbers,operators):

    cur = numbers[0]

    for i in range(len(numbers)-1):
        if operators[i] == "*":
            cur = cur * numbers[i+1]
        elif operators[i] == "+":
            cur = cur + numbers[i+1]
        elif operators[i] == "||":
            cur = int(str(cur) + str(numbers[i+1]))

    if cur == final:
        return True


def buildFunction(final,numbers,operators):

    if len(operators) == len(numbers) - 1:
        if calculateFunction(final,numbers,operators):
            return True
        else:
            return False

    operators.append("*")
    if buildFunction(final,numbers,operators):
        return True
    operators.pop()
    
    operators.append("+")
    if buildFunction(final,numbers,operators):
        return True
    operators.pop()

    operators.append("||")
    if buildFunction(final,numbers,operators):
        return True
    operators.pop()

    return False

for i in equations:

    final = i[0]
    numbers = i[1:]
    if buildFunction(final,numbers,[]):
        res += final

print(res)
