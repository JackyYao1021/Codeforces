from random import randint
 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

MOD = 10 ** 9 + 7

def bfs(adj):
    start = 1
    layers = [] 
    queue = [start]
    while queue:
        next_queue = []
        for u in queue:
            if adj[u-1][0] == 0:
                continue
            for a in adj[u-1]:
                next_queue.append(a)
        layers.append(queue)
        queue = next_queue
    return layers


def solve(n, adj, parents):
    layers = bfs(adj)
    layers.reverse()
    mem = [-1] * (n+1)
    
    for layer in layers:
        for node in layer:
            if adj[node-1][0] == 0:
                mem[node] = 0
            else:
                mem[node] = (4 + mem[adj[node-1][0]] + mem[adj[node-1][1]]) % MOD
    ans = [0] * (n+1) 
    ans[1] = (mem[1]+ 1) % MOD
    queue = [1]
    while queue:
        u = queue.pop()
        l, r = adj[u-1][0], adj[u-1][1]
        if l != 0:
            ans[l] = (ans[u] + mem[l] + 1) % MOD
            queue.append(l)
        if r != 0:
            ans[r] = (ans[u] + mem[r] + 1) % MOD
            queue.append(r)
    
    print(*ans[1:])
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        adj = [] * (n+1)
        parents = [0] * (n+1)
        for i in range(n):
            l, r = map(int, input().split())
            adj.append([l, r])
            parents[l] = i+1
            parents[r] = i+1
        solve(n, adj, parents)
        
