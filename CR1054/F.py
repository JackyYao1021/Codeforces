import math

def solve(h, d):
    h -= 1
    steps = int((math.isqrt(1 + 8*h) - 1) // 2)
    if steps >= d:
        return d
    ans = steps
    h -= steps * (steps + 1) // 2
    d -= steps
    while h >= 2 and d >= 2:
        d -= 2
        ans += 3
        h -= 2
    if d > 0:
        ans += d * 2
    return ans

t = int(input())
for _ in range(t):
    h, d = map(int, input().split())
    print(solve(h, d))
