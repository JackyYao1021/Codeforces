MOD = 998244353

def solve(n, x):
    zero_before = 1 + (x - 1 + 1) // 4
    one_before = (x - 1 + 3) // 4
    zero_after = 1 + (n + 1) // 4 - zero_before
    one_after = (n + 3) // 4 - one_before
    
    ans = (zero_before % MOD * zero_after % MOD) + (one_before % MOD * one_after % MOD)
    print(ans % MOD)

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    solve(n, x)
