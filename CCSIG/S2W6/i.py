MOD = 10**9 + 7

def solve(t, k, test, mx):
    dp = [1 for _ in range(mx+1)]
    
    for i in range(k, mx+1):
        dp[i] = (dp[i-k] + dp[i-1]) % MOD
    
    ans = [0] * (mx+1)
    for i in range(1, mx+1):
        ans[i] = (ans[i-1] + dp[i]) % MOD
        
    for a, b in test:
        print((ans[b] - ans[a-1]) % MOD)



    
    
    
    
    
    




if __name__ == "__main__":
    t, k = map(int, input().split())
    test = []
    mx = 0
    for _ in range(t):
        a, b = map(int, input().split())
        test.append((a, b))
        mx = max(mx, b)
    solve(t, k, test, mx)