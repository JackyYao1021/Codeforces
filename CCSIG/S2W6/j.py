def solve(n, arr):
    if n == 1:
        print(arr[0])
        return
    
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = dp[0] + arr[2]
    for i in range(3, n):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)