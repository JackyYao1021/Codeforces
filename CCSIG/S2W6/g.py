def solve(n, a, b, c):
    dp = [0] * (max(n, a, b, c)+1)
    a, b, c = sorted([a, b, c])
    dp[a] = 1
    dp[b] = 1
    dp[c] = 1
    for i in range(a, n+1):
        if dp[i-a] > 0:
            dp[i] = max(dp[i], dp[i-a] + 1)
        if i >= b and dp[i-b] > 0:
            dp[i] = max(dp[i], dp[i-b] + 1)
        if i >= c and dp[i-c] > 0:
            dp[i] = max(dp[i], dp[i-c] + 1)
    print(dp[n])
            


if __name__ == "__main__":
    n, a, b, c = map(int, input().split())
    solve(n, a, b, c)