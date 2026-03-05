def solve(n, h, k, arr):
    total = sum(arr)
    ans = 0
    if h > total:
        times = (h - 1) // total
        ans += times * (n+k)
        h -= total * times
    
    
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
    
    min_prefix = [float('inf')] * (n+1)
    cur_min = float('inf')
    for i in range(1, n+1):
        cur_min = min(cur_min, arr[i-1])
        min_prefix[i] = cur_min
    
        
    max_suffix = [0] * (n+1)
    cur_max = 0
    for i in range(n-1, -1, -1):
        cur_max = max(cur_max, arr[i])
        max_suffix[i] = cur_max
    
    idx = n-1
    
    for i in range(1, n+1):
        if prefix_sum[i] >= h:
            idx = i
            break
        
        if prefix_sum[i] + max_suffix[i] - min_prefix[i] >= h:
            idx = i
            break
            
    ans += idx
    print(ans)
    
        
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):    
        n, h, k = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, h, k, arr)