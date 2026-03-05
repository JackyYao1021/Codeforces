from collections import defaultdict, deque
def solve(n, arr):
    dp = [0] * (len(arr)+1)
    max_vals = defaultdict(lambda: -float('inf'))

    for i, a in enumerate(arr):
        dp[i+1] = dp[i]
        best_prev = max_vals[a]
        if best_prev != -float('inf'):
            dp[i+1] = max(dp[i+1], best_prev + i + 1)

        cur_val = dp[i] - i
        max_vals[a] = max(max_vals[a], cur_val)

    return dp[n]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(n, arr))