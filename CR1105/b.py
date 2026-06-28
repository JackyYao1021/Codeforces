MOD = 998244353

def solve():
    n, m, r, c = map(int, input().split())
    fixed = n*m - (n - r + 1) * (m - c + 1)
    print(pow(2, fixed, MOD))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()