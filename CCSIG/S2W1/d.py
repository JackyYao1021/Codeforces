def solve(n, arr):
    dp = arr.copy()
    
    partity_list = [a % 2 for a in arr]
    for i in range(1, n):
        if partity_list[i] != partity_list[i-1]:
            dp[i] = max(dp[i], dp[i-1] + arr[i])
    print(max(dp))
                


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)
        