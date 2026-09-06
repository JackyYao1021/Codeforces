def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    canput = [True] * n
    ans = [0] * n
    
    covers = [0] * (n+1)
    for i in range(n):
        if arr[i] == 0 or arr[i] == -1:
            continue
        else:
            left = max(0, i - arr[i]+1)
            right = min(n - 1, i + arr[i]-1)
            covers[left] += 1
            covers[right + 1] -= 1
    
    cover_cnt = 0
    for i in range(n):
        cover_cnt += covers[i]
        if cover_cnt > 0:
            canput[i] = False
    
    for i in range(n):
        if canput[i]:
            ans[i] = 1
        else:
            ans[i] = 0
    
    for i in range(n):
        if arr[i] == -1:
            continue
        if not ((i - arr[i] >= 0 and ans[i - arr[i]] == 1) or (i + arr[i] <= n-1 and ans[i + arr[i]] == 1)):
            print(-1)
            return
    print("".join(map(str, ans)))
            
        
        
            
    
    
        




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()