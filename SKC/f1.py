from collections import deque

def solve(n, m, grid):

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    visited = [[[[False] * 2 for _ in range(4)] for _ in range(m)] for _ in range(n)]
    
    queue = deque()

    for d in range(4):
        if grid[0][0] != 0:
            queue.append((0, 0, d, 0, 0))
            visited[0][0][d][0] = True

    while queue:
        x, y, direction, smile, steps = queue.popleft()

        if x == m-1 and y == n-1:
            print(steps)
            return

        curr_type = grid[y][x]

        if curr_type == 4:
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
            
            
            if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] in [1, 2, 4]:
                if not visited[ny][nx][direction][0]:
                    visited[ny][nx][direction][0] = True
                    queue.append((nx, ny, direction, 0, steps + 1))
                continue
            
            
            new_smile = 0 
        elif curr_type == 3:
            if smile == 0: continue
            new_smile = 1
        elif curr_type == 2:
            new_smile = 1 
        else:
            new_smile = smile

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] != 0:
                if not visited[ny][nx][i][new_smile]:
                    visited[ny][nx][i][new_smile] = True
                    queue.append((nx, ny, i, new_smile, steps + 1))

    print("-1")

if __name__ == "__main__":
    
    n, m = map(int, input().split())    
    grid = [list(map(int, input().split())) for _ in range(n)]
    solve(n, m, grid)