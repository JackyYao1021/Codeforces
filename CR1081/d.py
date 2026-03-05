def solve(n, vals, edges):
        
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    subtree_sum = [0] * (n + 1)
    init_cost = [0] * (n + 1)
    depth = [0] * (n + 1)
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]

    def dfs_init(u, p, d):
        depth[u] = d
        parent[u] = p
        subtree_sum[u] = vals[u-1]
        cost = 0
        for v in adj[u]:
            if v == p: continue
            children[u].append(v)
            dfs_init(v, u, d + 1)
            subtree_sum[u] += subtree_sum[v]
            cost += init_cost[v] + subtree_sum[v]
        init_cost[u] = cost

    dfs_init(1, -1, 0)

    results = []
    for r in range(1, n + 1):
        max_rel_depth = 0
        stack = [(r, 0)]
        subtree_nodes = []
        while stack:
            curr, d_rel = stack.pop()
            subtree_nodes.append((curr, d_rel))
            if d_rel > max_rel_depth:
                max_rel_depth = d_rel
            for v in children[curr]:
                stack.append((v, d_rel + 1))
        
        max_delta = 0
        for u, d_rel_u in subtree_nodes:
            if u == r: continue
            delta = subtree_sum[u] * (max_rel_depth + 1 - d_rel_u)
            if delta > max_delta:
                max_delta = delta
        
        results.append(init_cost[r] + max_delta)
        
    print(*results)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):    
        n = int(input())
        vals = list(map(int, input().split()))
        edges = []
        for _ in range(n-1):
            u, v = map(int, input().split())
            edges.append((u, v))
        solve(n, vals, edges)