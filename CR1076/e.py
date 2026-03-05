from collections import deque
from bisect import bisect_right
from random import randint
 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

def solve(n, arr):
    dist = [-1] * (n + 1)
    arr = [Wrapper(a) for a in arr]
    s = set(arr)
    if 1 in s:
        dist[1] = 1
        s.discard(1) 

    factors = sorted(x for x in s if x <= n)
    q = deque()

    for x in factors:
        dist[x] = 1
        q.append(x)

    while q:
        curr = q.popleft()
        lim = n // curr
        k = bisect_right(factors, lim)
        base = dist[curr] + 1

        for i in range(k):
            nxt = curr * factors[i]
            if dist[nxt] == -1:
                dist[nxt] = base
                q.append(nxt)

    print(*dist[1:])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)
