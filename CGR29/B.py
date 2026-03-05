from math import ceil


def R(l):
    return list(reversed(l))


def langford_davies(n):
    x = ceil(n/4)
    a, b, c, d = 2*x-1, 4*x-2, 4*x-1, 4*x
    p = [i for i in range(1, a) if i % 2 == 1]
    q = [i for i in range(2, a) if i % 2 == 0]
    r = [i for i in range(a+2, b) if i % 2 == 1]
    s = [i for i in range(a+1, b) if i % 2 == 0]
    if n % 4 == 0:
        return R(s) + R(p) + [b] + p + [c] + s + [d] + R(r) + R(q) + [b, a] + q + [c]  + r + [a, d]
    if n % 4 == 3:
        return R(s) + R(p) + [b] + p + [c] + s + [a] + R(r) + R(q) + [b, a] + q + [c]  + r
    return None


t = int(input())
for _ in range(t):
    n = int(input())
    print(*langford_davies(n))
