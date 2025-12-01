import sys

pos = 50
hits = 0

for line in sys.stdin:
    line = line.strip()

    move, dist = line[0], int(line[1:])
    
    step = -1 if move == 'L' else 1

    for _ in range(dist):
        pos = (pos + step) % 100
        if pos == 0:
            hits += 1

print(hits)
    