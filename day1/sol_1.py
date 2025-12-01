import sys

pos = 50
res = [pos]
i = 0

for line in sys.stdin:
    line = line.strip()

    move, dist = line[0], int(line[1:])
    temp = 0

    if move == 'L':
        temp = (res[i] - dist) % 100
    else:
        temp = (res[i] + dist) % 100
    res.append(temp)
    i += 1

print(res.count(0))
    