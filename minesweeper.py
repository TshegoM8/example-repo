def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    result = []
    
    for i in range(rows):
        row_result = []
        for j in range(cols):
            if grid[i][j] == "#":
                row_result.append("#")
            else:
                
                count = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == "#":
                            count += 1
                row_result.append(count)
        result.append(row_result)
    
    return result

input = [
    ["#", "#", "#", "-", "-"],
    ["#", "#", "-", "#", "-"],
    ["-", "-", "#", "#", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "-", "#", "-", "-"]
]

output = minesweeper(input)

for row in output:
    print(row)
