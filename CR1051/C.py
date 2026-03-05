from collections import deque
def solve():
    n = int(input())
    adj = [[] for _ in range(n+1)]
    in_deg = [0] * (n+1)
    for _ in range(n-1):
        u, v, x, y = map(int, input().split())
        if x > y:
            adj[v].append(u)
            in_deg[u] += 1
        else:
            adj[u].append(v)
            in_deg[v] += 1
            
    queue = deque([i for i in range(1, n+1) if in_deg[i] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            in_deg[neighbor] -= 1
            if in_deg[neighbor] == 0:
                queue.append(neighbor)
    
    ans = [0] * (n+1)
    for i, ord in enumerate(order):
        ans[ord] = i + 1

    return ans[1:]

t = int(input())
for _ in range(t):
    print(*solve())