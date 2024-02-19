def direction_in_grid(n, m):
    grid = [['' for _ in range(m)] for _ in range(n)]
    visited = set()

    def is_valid_move(r, c):
        return 0 <= r < n and 0 <= c < m and (r, c) not in visited

    def update_location(direction, r, c):
        while is_valid_move(r, c):
            visited.add((r, c))
            grid[r][c] = direction
            r, c = move(direction, r, c)

    def move(direction, r, c):
        if direction == 'R':
            c += 1
        elif direction == 'D':
            r += 1
        elif direction == 'L':
            c -= 1
        elif direction == 'U':
            r -= 1
        return r, c

    location = 'R'
    for i in range(n):
        update_location(location, i, 0)
        update_location(location, i, m - 1)

    for j in range(m):
        update_location(location, 0, j)
        update_location(location, n - 1, j)

    return location

# Example usage:
direction = direction_in_grid(1000, 1000)
print(direction)