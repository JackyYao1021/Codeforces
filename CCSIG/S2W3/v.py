from bisect import bisect_right
def solve(n, k, arr):
    arr.sort()
    arr = arr[n//2:]
    n = len(arr)
    
    sum_arr = [0] * n
    sum_arr[0] = arr[0]
    targets = [0] * n
    
    for i in range(1, n):
        targets[i] = arr[i] * i - sum_arr[i-1]
        sum_arr[i] = sum_arr[i-1] + arr[i]
        
    idx = bisect_right(targets, k)
    
    rest = k - targets[idx-1]
    print(arr[idx-1] + rest // idx) 
    


if __name__ == "__main__":
    
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    solve(n, k, arr)
        