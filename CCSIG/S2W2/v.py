from collections import defaultdict
class DSU():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            if self.rank[pa] < self.rank[pb]:
                pa, pb = pb, pa
            self.parent[pb] = pa
            if self.rank[pa] == self.rank[pb]:
                self.rank[pa] += 1
        else:
            return False
        return True


def solve(n, roads):
    dsu = DSU(n)
    redundant = []
    for a, b in roads:
        if not dsu.union(a, b):
            redundant.append((a, b))
        
    parents = set()
    for i in range(n):
        parent = dsu.find(i)
        parents.add(parent)
        
    parents = list(parents)
    start = parents[0]
    print(len(parents)-1)
    for i in range(1, len(parents)):
        print(redundant[i-1][0]+1, redundant[i-1][1]+1, start+1, parents[i]+1)
                
            
    
    
        
        
    

if __name__ == "__main__":
    n = int(input())
    roads = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        roads.append((a-1, b-1))
    solve(n, roads)