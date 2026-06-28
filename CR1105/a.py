from math import log

def solve():
    n, k = map(int, input().split())
    cost = 1
    ans = 0
    while cost <= n:
        ans += min(k, n // cost)
        n -= min(k, n // cost) * cost
        cost *= 2
    print(ans)
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()