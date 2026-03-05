from collections import defaultdict
def solve(n, arr, brr):
    # dp = [[0 for _ in range(4)] for _ in range(2)]

    # for i in range(n):
    #     new_dp = [0 for _ in range(4)]        
    #     # not pick, pick arr, pick brr, pick both
    #     new_dp[0] = max(dp[0][0], dp[0][1], dp[0][2], dp[0][3], dp[1][0], dp[1][1], dp[1][2], dp[1][3])
    #     new_dp[1] = max(dp[0][0], dp[0][1], dp[0][2], dp[0][3], dp[1][0], dp[1][2]) + arr[i]
    #     new_dp[2] = max(dp[0][0], dp[0][1], dp[0][2], dp[0][3], dp[1][0], dp[1][1]) + brr[i]
    #     new_dp[3] = max(dp[0][0], dp[0][1], dp[0][2], dp[0][3]) + arr[i] + brr[i]
    #     dp[0] = dp[1]
    #     dp[1] = new_dp
    
    # if n % 2 == 0:
    #     print(max(dp[1][0], dp[1][1], dp[1][2], dp[1][3]))
    # else:
    #     print(max(dp[1][1], dp[1][2]))
    
    dp = [[0 for _ in range(3)] for _ in range(2)]
    for i in range(n):
        new_dp = [0 for _ in range(3)]
        new_dp[0] = max(dp[0][0], dp[0][1], dp[0][2], dp[1][0], dp[1][1], dp[1][2])
        new_dp[1] = max(dp[0][0], dp[0][1], dp[0][2], dp[1][0], dp[1][2]) + arr[i]
        new_dp[2] = max(dp[0][0], dp[0][1], dp[0][2], dp[1][0], dp[1][1]) + brr[i]
        dp[0] = dp[1]
        dp[1] = new_dp
        
    print(max(dp[1][0], dp[1][1], dp[1][2]))
        
        
    

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    solve(n, arr, brr)