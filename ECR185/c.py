def solve(n, k, qs, rs):
    qs.sort()
    rs.sort()
    idx_q = 0
    idx_r = n  - 1
    ans = 0

    while idx_q < n and idx_r >= 0:
        if (qs[idx_q] + 1) * (rs[idx_r] + 1) <= k+1:
            ans += 1
            idx_q += 1
            idx_r -= 1
        else:
            idx_r -= 1
    return ans
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        qs = list(map(int, input().split()))
        rs = list(map(int, input().split()))
        print(solve(n, k, qs, rs))