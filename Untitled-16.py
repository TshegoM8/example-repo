def is_valid_position(grid, row, col):
    """Check if the given row and col are within the bounds of the grid."""
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def count_adjacent_mines(grid, row, col):
    """Count how many mines are adjacent to the cell at (row, col)."""
    mine_count = 0
    # All 8 possible directions
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        if is_valid_position(grid, new_row, new_col) and grid[new_row][new_col] == "#":
            mine_count += 1

    return mine_count

def minesweeper_grid(grid):
    """Return a new grid with mine counts for each non-mine cell."""
    result = []

    for row_index, row in enumerate(grid):
        new_row = []
        for col_index, cell in enumerate(row):
            if cell == "#":
                new_row.append("#")
            else:
                count = count_adjacent_mines(grid, row_index, col_index)
                new_row.append(count)
        result.append(new_row)

    return result
