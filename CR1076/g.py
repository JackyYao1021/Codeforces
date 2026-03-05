from collections import defaultdict
from collections import deque
from sys import stdout
def lca_preprocess(adj, root, nodes):
    parent = {root: root}
    depth = {root: 0}
    order = [root]
    q = deque([root])

    while q:
        u = q.popleft()
        for v in adj[u]:
            if v in parent:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            q.append(v)
            order.append(v)

    LOG = (len(nodes) + 1).bit_length()
    up = [dict() for _ in range(LOG)]
    for x in order:
        up[0][x] = parent[x]
    for k in range(1, LOG):
        for x in order:
            up[k][x] = up[k-1][ up[k-1][x] ]

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        diff = depth[a] - depth[b]
        k = 0
        while diff:
            if diff & 1:
                a = up[k][a]
            diff >>= 1
            k += 1
        if a == b:
            return a
        for k in range(LOG - 1, -1, -1):
            if up[k][a] != up[k][b]:
                a = up[k][a]
                b = up[k][b]
        return parent[a]

    return parent, lca

def get_path(a, b, parent, lca_fn):
    c = lca_fn(a, b)

    left = []
    x = a
    while x != c:
        left.append(x)
        x = parent[x]
    left.append(c)

    right = []
    y = b
    while y != c:
        right.append(y)
        y = parent[y]
    right.reverse()

    return left + right



def solve(adj, nodes):
    # Find a starting point (a node with degree 1)
    start = set()
    for node, nex in adj.items():
        if len(nex) == 1:
            start.add(node)
    
    root = next(iter(nodes))
    parent, lca_fn = lca_preprocess(adj, root, nodes)
    
    traces = []
    start = list(start)
    L = len(start)
    start_pairs = []
    if L == 2:
        start_pairs = [(start[0], start[0]), (start[1], start[1])]
    else:
        for i in range(0, L//2, 2):
            start_pairs.append((start[2*i], start[2*i+1]))
        if L % 2 == 1:
            start_pairs.append((start[0], start[-1]))
        
    found = False
    while not found:
        while start_pairs:
            a, b = start_pairs.pop()
            path = get_path(a, b, parent, lca_fn)
            print(f"? {a} {b}")
            stdout.flush()
            res = int(input())
            if len(path) == 1 and res:
                print(f"! {path[0]}")
                stdout.flush()
                found = True
                break
            if res:
                if len(path) == 2:
                    print(f"? {a} {a}")
                    stdout.flush()
                    res2 = int(input())
                    if res2:
                        print(f"! {a}")
                    else:
                        print(f"! {b}")
                    stdout.flush()
                    found = True
                    break   
                else:
                    start_pairs = [(path[len(path) // 2-1], a), (path[len(path) // 2], b)]
    
        
        
    
    
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        adj = defaultdict(list)
        nodes = set()
        for _ in range(n-1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            nodes.add(u)
            nodes.add(v)
        solve(adj, nodes)