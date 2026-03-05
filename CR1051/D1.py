MOD = 10**9 + 7

class BIT():
    def __init__(self, size, mod):
        self.size = size
        self.mod = mod
        self.tree = [0] * (size + 1)
    def add(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] = (self.tree[idx] + delta) % self.mod
            idx += idx & -idx
    def query(self, idx):
        res = 0
        while idx > 0:
            res = (res + self.tree[idx]) % self.mod
            idx -= idx & -idx
        return res
    
    
def solve(a):
    n = int(input())
    if n == 0:
        return 1
    

t = int(input())
for _ in range(t):
    print(solve())