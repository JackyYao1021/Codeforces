import math
def solve(n, a):
    
    MOD = 998244353
    MAXN = 50

    fac = [1] * (MAXN + 1)
    invfac = [1] * (MAXN + 1)

    for i in range(1, MAXN + 1):
        fac[i] = fac[i-1] * i % MOD

    invfac[MAXN] = pow(fac[MAXN], MOD-2, MOD)
    for i in range(MAXN, 0, -1):
        invfac[i-1] = invfac[i] * i % MOD

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fac[n] * invfac[k] % MOD * invfac[n-k] % MOD

    
    
    mx = max(a[1:])
    mx_cnt = 0
    for i in range(1, n+1):
        if a[i] < mx-1:
            a[0] -= (mx-1) - a[i]
            a[i] = mx -1
        elif a[i] == mx:
            mx_cnt += 1
        if a[0] < 0:
            return 0
    
    if a[0] >= n-mx_cnt:
        a[0] -= (n - mx_cnt)
        a[0] %= n
        return fac[n]
    
    else:
        res = comb(n - mx_cnt, a[0])
        res = res * fac[a[0] + mx_cnt] % MOD
        res = res * fac[n - mx_cnt - a[0]] % MOD
        return res

            

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(n, a))