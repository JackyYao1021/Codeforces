MOD = 998244353
    
def solve():
    n = int(input())
    parents = [-1] * n
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    
    root = n-1
    stack = [root]
    leaves = []
    while stack:
        node = stack.pop()
        if node != root and len(adj[node]) == 1:
            leaves.append(node)
        for neighbor in adj[node]:
            if neighbor != parents[node]:
                parents[neighbor] = node
                stack.append(neighbor)
    
        
        
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()