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


def helper(v, k, adj, parents, mem):
    pass



def solve(n, q, queries, adj, parents):
    layers = bfs(adj)
    layers.reverse()
    mem = [-1] * (n+1)
    
    for layer in layers:
        for node in layer:
            if adj[node-1][0] == 0:
                mem[node] = 0
            else:
                mem[node] = (4 + mem[adj[node-1][0]] + mem[adj[node-1][1]]) % MOD
    
    print(mem)
    for v, k in queries:
        while k > 0 and v != 1:
            if k > mem[v]:
                k -= mem[v] + 1
                v = parents[v]
            else:
                l, r = adj[v-1][0], adj[v-1][1]
                

    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        adj = [] * (n+1)
        parents = [0] * (n+1)
        for i in range(n):
            l, r = map(int, input().split())
            adj.append([l, r])
            parents[l] = i+1
            parents[r] = i+1
        queries = []
        for _ in range(q):
            v, k = map(int, input().split())
            queries.append((v, k))
        solve(n, q, queries, adj, parents)
        
