with open("input.txt") as f:
    grid = [list(line.rstrip("\n")) for line in f]

rows = len(grid)
cols = len(grid[0])

start_col = None
for col in range(cols):
    if grid[0][col] == "S":
        start_col = col
        break

timelines = {start_col: 1}  # column -> split count

for row in range(1, rows):
    new_timelines = {}

    for col, count in timelines.items():
        if col < 0 or col >= cols:
            continue
        
        cell = grid[row][col]

        if cell == ".":
            #particle continues downward, timelines preserved
            new_timelines[col] = new_timelines.get(col, 0) + count
        elif cell == "^":
            left_col = col - 1
            new_timelines[left_col] = new_timelines.get(left_col, 0) + count
            right_col = col + 1
            new_timelines[right_col] = new_timelines.get(right_col, 0) + count
    
    timelines = new_timelines

    if not timelines:
        break

total_timelines = sum(timelines.values())
print(total_timelines)