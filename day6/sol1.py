with open('input.txt') as f:
    lines = f.readlines()

matrix = []
for line in lines:
    row = list(line.split())
    matrix.append(row)

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

ROWS, COLS = len(transposed), len(transposed[0])
res = []

for r in range(ROWS):
    total = 0
    if transposed[r][COLS - 1] == '+':
        for i in range(COLS - 1):
            total += int(transposed[r][i])
        res.append(total)

    elif transposed[r][COLS - 1] == '*':
        total = 1
        for i in range(COLS - 1):
            total *= int(transposed[r][i])
        res.append(total)

print(sum(res))