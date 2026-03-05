def solve(n):
    idx = 1
    tmp = 1
    visited = set()
    visited.add(1)
    while idx <= n**2:
        nxt = idx + tmp
        tmp += 1
        if nxt > n**2:
            break
        visited.add(nxt)
        idx = nxt
    
    list_visited = sorted(list(visited))
    rest = [i for i in range(1, n**2 + 1) if i not in visited]
    
    if_reverse = False
    while len(list_visited) >= n:
        if if_reverse:
            print(*list_visited[:n][::-1])
            if_reverse = False
        else:
            print(*list_visited[:n])
            if_reverse = True
        list_visited = list_visited[n:]
    
    if list_visited:
        if if_reverse:
            print(*(list_visited[::-1]+rest[:n-len(list_visited)]))
        else:
            print(*(list_visited+rest[:n-len(list_visited)]))
        rest = rest[n-len(list_visited):]
    
    while len(rest) >= n:
        print(*rest[:n])
        rest = rest[n:]
    
    
    
    
            
            


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)