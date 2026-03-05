import math

def get_cost(sub_array):
    if not sub_array:
        return 0
        
    sub_array.sort()
    n = len(sub_array)
    
    median = sub_array[n // 2]
    
    cost = 0
    for x in sub_array:
        cost += abs(x - median)
    return cost

def solve_nice_array(a):
    n = len(a)
    
    if n < 2:
        return float('inf') 

    costs = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            sub = a[i : j+1]
            costs[i][j] = get_cost(sub)

    dp = [[float('inf')] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            dp[i][j] = costs[i][j]
            
            if length >= 4:
                for k in range(i + 1, j - 1):
                    if dp[k+1][j] != float('inf'):
                         dp[i][j] = min(dp[i][j], costs[i][k] + dp[k+1][j])

    min_ops = dp[0][n-1]

    for k in range(n - 1):
        for j in range(k + 2, n):

            wrap_block = a[j:] + a[:k+1]
            wrap_cost = get_cost(wrap_block)
            
            inner_cost = 0
            inner_len = j - 1 - k
            
            if inner_len == 1:
                continue
            
            if inner_len >= 2:
                inner_cost = dp[k+1][j-1]
            
            min_ops = min(min_ops, wrap_cost + inner_cost)

    return min_ops
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve_nice_array(arr))
        