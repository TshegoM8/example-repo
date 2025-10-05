def mine_sweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = []

    for i in range(rows):
        new_row = []
        for j in range(cols):
            if grid[i][j] == '#':
                new_row.append('#')
            else:
                mine_count = 0
                # Check all 8 surrounding cells
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x == 0 and y == 0:
                            continue  # Skip the current cell
                        ni, nj = i + x, j + y
                        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '#':
                            mine_count += 1
                new_row.append(str(mine_count))
        result.append(new_row)

    return result
