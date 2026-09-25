def solve():
    n, k = map(int, input().split())
    ans = [[0 for _ in range(n)] for _ in range(n)]
    if k < n or k == 2*n:
        print(-1)
        return
    else:
        d = k - n
        # print(d)
        for i in range(n - d):
            ans[i][i] = i + 1
        
        for i in range(n - d, n):
            ans[n-d-1][i] = i + 1
        
    nxt = n+1
    for i in range(n):
        for j in range(n):
            if ans[i][j] == 0:
                ans[i][j] = nxt
                nxt += 1

    for i in range(n):
        print(*ans[i])
        




# 3, 4, 5, 6
# 1 2 3
# 4   
# 5    

# 1 5 6
# 4 2 3
#   4 5

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()