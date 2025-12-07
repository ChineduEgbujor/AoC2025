with open("input.txt") as f:
    grid = [list(line) for line in f.read().splitlines()]
    
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0) , (-1, -1), (-1, 1)]

    ROWS, COLS = len(grid), len(grid[0])
    total = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "@":
                count = 0
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < ROWS and 0 <= cc < COLS and grid[rr][cc] == "@":
                        count += 1
                if count < 4:
                    total += 1
    print("total", total)
                



