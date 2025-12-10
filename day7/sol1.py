with open("input.txt") as f:
    grid = [list(line.rstrip('\n')) for line in f]

rows = len(grid)
cols = len(grid[0])

# find the starting position S
start_col = None
for col in range(cols):
    if grid[0][col] == 'S':
        start_col = col
        break

active_beams = {start_col}
split_count = 0

for row in range(1, rows):
    new_beams = set()

    for col in active_beams:
        if col < 0 or col >= cols:
            continue

        cell = grid[row][col]

        if cell == '.':
            new_beams.add(col)
        elif cell == '^':
            split_count += 1
            new_beams.add(col - 1)
            new_beams.add(col + 1)

    active_beams = new_beams

    if not active_beams:
        break


print(split_count)