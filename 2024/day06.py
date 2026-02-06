def simulate_guard_path(lines):
    grid = [list(line.strip()) for line in lines]
    rows, cols = len(grid), len(grid[0])

    # Directions in order: Up, Right, Down, Left
    # Each tuple = (dx, dy) meaning change in (column, row)
    # NOTE: Here (x = col, y = row), so (0, -1) means "up" one row.
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # Map guard symbol to starting facing direction index
    dir_maps = {"^": 0, ">": 1, "v": 2, "<": 3}

    visited = set()

    # Find the guard's starting position (x = col, y = row)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in dir_maps:
                x, y = c, r
                break

    # Initial facing direction
    dir_index = dir_maps[grid[y][x]]

    while True:
        # Record current position
        visited.add((x, y))

        # Calculate next position based on current direction
        dx, dy = dirs[dir_index]
        nx, ny = x + dx, y + dy

        # If next step is outside the grid, stop simulation
        if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
            break

        # If there's an obstacle, turn right (90 degrees clockwise)
        if grid[ny][nx] == "#":
            dir_index = (dir_index + 1) % 4
            continue

        # Move forward
        x, y = nx, ny

    return len(visited)


def guard_loops_with_obstacle(grid, start_x, start_y, start_dir):
    rows, cols = len(grid), len(grid[0])
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left
    x, y, dir_index = start_x, start_y, start_dir
    seen_states = set()

    while True:
        state = (x, y, dir_index)
        if state in seen_states:
            return True  # Loop detected
        seen_states.add(state)

        dx, dy = dirs[dir_index]
        nx, ny = x + dx, y + dy

        # Out of bounds → guard leaves
        if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
            return False

        # Obstacle → turn right
        if grid[ny][nx] == "#":
            dir_index = (dir_index + 1) % 4
        else:
            x, y = nx, ny


def count_obstacle_positions(lines):
    grid = [list(row.strip()) for row in lines]
    rows, cols = len(grid), len(grid[0])
    dir_map = {"^": 0, ">": 1, "v": 2, "<": 3}

    # Find starting position & direction
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] in dir_map:
                start_x, start_y = x, y
                start_dir = dir_map[grid[y][x]]
                break

    count = 0
    for y in range(rows):
        for x in range(cols):
            if (x, y) == (start_x, start_y):
                continue
            if grid[y][x] != ".":
                continue

            # Place obstacle
            grid[y][x] = "#"
            if guard_loops_with_obstacle(grid, start_x, start_y, start_dir):
                count += 1
            grid[y][x] = "."  # Restore

    return count


def main(lines):
    res = simulate_guard_path(lines)
    res2 = count_obstacle_positions(lines)

    print(f"The guard visits {res} distinct positions.")
    print(f"The guard loops with {res2} obstacle positions.")
