from collections import deque
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(n, m, grid, states, visited, steps):
    new_states = []
    states = deque(states)

    while states:
        x, y, direction, smile = states.popleft()

        if not (0 <= x < m and 0 <= y < n):
            continue

        if x == m-1 and y == n-1:
            return steps, True, new_states, visited

        if grid[y][x] == 0:
            continue

        state = (x, y, direction, smile)
        if state in visited:
            continue
        
        visited.add(state)

        if grid[y][x] == 1:
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_states.append((nx, ny, i, smile))

        elif grid[y][x] == 2:
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_states.append((nx, ny, i, 1))

        elif grid[y][x] == 3:
            if smile == 1:
                for i, (dx, dy) in enumerate(directions):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        new_states.append((nx, ny, i, smile))

        elif grid[y][x] == 4:
            nx = x + directions[direction][0]
            ny = y + directions[direction][1]
            
            if 0 <= nx < m and 0 <= ny < n:
                nxt = grid[ny][nx]
                if nxt == 1 or nxt == 2 or nxt == 4:
                    new_states.append((nx, ny, direction, 0))
                    continue
            
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_states.append((nx, ny, i, 0))
            
    return steps + 1, False, new_states, visited



def solve(n, m, grid):
    visited = set()
    
    states = [(0, 0, d, 0) for d in range(4)]
    steps = 0
    while True:
        steps, found, states, visited = bfs(n, m, grid, states, visited, steps)
        if found:
            return steps
        if not states:
            return -1    
    
                
if __name__ == "__main__":
    n, m = map(int, input().split())    
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, grid))