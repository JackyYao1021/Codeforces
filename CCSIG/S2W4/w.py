from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solve(n, m, k, grid):
    start = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                start = (i, j)
                break
        if start:
            break

    visited = set([start])
    q = [start]
    layers = []

    layers.append([start])

    while q:
        nq = []
        for x, y in q:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "." and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    nq.append((nx, ny))
        if not nq:
            break
        layers.append(nq)
        q = nq

    while k > 0 and layers:
        layer = layers.pop()
        for x, y in layer:
            if k == 0:
                break
            grid[x][y] = "X"
            k -= 1

    for row in grid:
        print("".join(row))
        
        


if __name__ == "__main__": 
    n, m, k = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append([x for x in input().strip()])
    solve(n, m, k, grid)