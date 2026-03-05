from collections import Counter
import sys

MOD = 998244353

def build_fact(max_n: int):
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact = [1] * (max_n + 1)
    invfact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    return fact, invfact

def solve_case(n, arr, fact):
    cnt = Counter(arr)
    mx = max(cnt)
    cnt_mx = cnt[mx]

    if cnt_mx >= 2:
        return fact[n]

    # mx occurs exactly once
    second = None
    for v in cnt:
        if v != mx:
            if second is None or v > second:
                second = v

    if mx - second > 1:
        return 0

    c = cnt[second]
    return fact[n] * c % MOD * pow(c + 1, MOD - 2, MOD) % MOD

if __name__ == "__main__":
    t = int(input())
    cases = []
    max_n = 0
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        cases.append((n, arr))
        if n > max_n:
            max_n = n

    fact, _ = build_fact(max_n)

    out = []
    for n, arr in cases:
        out.append(str(solve_case(n, arr, fact)))
    print("\n".join(out))