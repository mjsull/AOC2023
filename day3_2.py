import sys


matrix = []
adjacent = {}
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        matrix.append(line.rstrip())
        for x, letter in enumerate(line.rstrip()):
            if letter == '*':
                for xx in range(x-1, x+2):
                    for yy in range(y-1, y+2):
                        if not (xx, yy) in adjacent:
                            adjacent[(xx, yy)] = []
                        adjacent[(xx,yy)].append((x, y))

partnumbers = {}
for y, line in enumerate(matrix):
    number = ''
    coords = set()
    for x, letter in enumerate(line):
        if letter.isdigit():
            number += letter
            coords.add((x, y))
        else:
            if number != '':
                theset = set()
                for i in coords.intersection(adjacent):
                    for j in adjacent[i]:
                        theset.add(j)
                for i in theset:
                    if not i in partnumbers:
                        partnumbers[i] = []
                    partnumbers[i].append(int(number))
            number = ''
            coords = set()
    if number != '':
        theset = set()
        for i in coords.intersection(adjacent):
            for j in adjacent[i]:
                theset.add(j)
        for i in theset:
            if not i in partnumbers:
                partnumbers[i] = []
            partnumbers[i].append(int(number))

thesum = 0

for i in partnumbers:
    print(i, partnumbers[i])
    if len(partnumbers[i]) == 2:
        gear_ratio = partnumbers[i][0] * partnumbers[i][1]
        thesum += gear_ratio

print(thesum)
