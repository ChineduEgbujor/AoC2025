with open("input.txt") as f:
    grid = [list(line) for line in f.read().splitlines()]
    
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

    ROWS, COLS = len(grid), len(grid[0])
    total_removed = 0
    
    while True:
        # Find all rolls that can be removed this round (fewer than 4 neighbors)
        to_remove = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "@":
                    count = 0
                    for dr, dc in directions:
                        rr, cc = r + dr, c + dc
                        if 0 <= rr < ROWS and 0 <= cc < COLS and grid[rr][cc] == "@":
                            count += 1
                    if count < 4:
                        to_remove.append((r, c))
        
        # If no rolls can be removed, we're done
        if not to_remove:
            break
        
        # Remove all accessible rolls
        for r, c in to_remove:
            grid[r][c] = "."
        
        total_removed += len(to_remove)
        print(f"Removed {len(to_remove)} rolls of paper")
    
    print("Total removed:", total_removed)