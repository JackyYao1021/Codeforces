def solve(n, arr):
    dp = [[0, 0] for _ in range(n + 2)] # not sit / sit
    
    dp[n][0] = 0
    dp[n][1] = 1
    for i in range(n-1, 0, -1):
        if arr[i-1] > i:
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1])
            dp[i][1] = max(dp[i + 1][0], dp[i + 1][1]) + 1 - max(dp[arr[i-1]][0], dp[arr[i-1]][1])
        else:
            dp[i][0] = max(dp[i + 1][0], dp[i + 1][1])
            dp[i][1] = max(dp[i + 1][0], dp[i + 1][1]) + 1

    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, dp[i][0], dp[i][1])
    print(ans)  
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)