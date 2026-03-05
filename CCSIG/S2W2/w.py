from collections import Counter
big = float('inf')
class DSU():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.weights = [(big, 0)] * n
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b, w):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
        self.weights[pa] = (min(self.weights[pa][0], self.weights[pb][0], w), max(self.weights[pa][1], self.weights[pb][1], w))
        return True


def solve(n, m, paths):
    ans = [] 
    paths.sort(key=lambda x: x[2])
    dsu = DSU(n)
    for path in paths:
        u, v, w = path
        dsu.union(u, v, w)
        if dsu.find(0) == dsu.find(n-1):
            ans.append(dsu.weights[dsu.find(0)][1] + dsu.weights[dsu.find(0)][0])
    print(min(ans))
    return
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        paths = []
        for _ in range(m):
            u, v, w = list(map(int, input().split()))
            paths.append((u-1, v-1, w))
        solve(n, m, paths)
            
        