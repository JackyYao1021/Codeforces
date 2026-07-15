class UnionSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def solve():
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    dsu = UnionSet(n)
    for i in range(n):
        if i + x < n:
            dsu.union(i, i + x)
        if i + y < n:
            dsu.union(i, i + y)
    
    for i in range(n):
        if dsu.find(arr[i]-1) != dsu.find(i):
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()