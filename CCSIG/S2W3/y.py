from bisect import bisect_left, bisect_right
def solve(n, m, arr, brr):
    arr.sort()
    brr.sort()
    
    dic_a = {arr[0]: 0}
    dic_b = {brr[0]: 0}
    
    
    arr_prefix_sum = [0] * (n+1)
    
    
    for i in range(1, n+1):
        arr_prefix_sum[i] = arr_prefix_sum[i-1] + arr[i-1]
        dic_a[arr[i-1]] = i
        
    brr_prefix_sum = [0] * (m+1)
    
    for i in range(1, m+1):
        brr_prefix_sum[i] = brr_prefix_sum[i-1] + brr[i-1]
        dic_b[brr[i-1]] = i
    
    if arr[0] >= brr[-1]:
        print(0)
        return
    
    totalB = brr_prefix_sum[-1]
    ans = float('inf')
    candidates = set(arr) | set(brr)
    for x in candidates:
        k = bisect_left(arr, x)     
        idx = bisect_right(brr, x)

        costA = k * x - arr_prefix_sum[k]

        cntAbove = m - idx
        sumAbove = totalB - brr_prefix_sum[idx]
        costB = sumAbove - cntAbove * x

        ans = min(ans, costA + costB)
    print(ans)
        
    

if __name__ == "__main__":
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    solve(n, m, arr, brr)