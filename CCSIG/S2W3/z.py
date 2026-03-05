def count_have(arr, brr, mid):
    cnt = 0
    for a, b in zip(arr, brr):
        if a < mid:
            continue
        
        cnt += (a - mid - 1) // b + 1
        
    return cnt


def count_sum(arr, brr, mid):
    total = 0
    for a, b in zip(arr, brr):
        if a < mid:
            continue
        
        c = (a - mid - 1) // b + 1
        total += c * a - b * (c * (c - 1) // 2)
        
    return total

def solve(n, k, arr, brr):
    
    left = 0
    right = max(arr)+1
    
    while left < right:
        mid = (left + right) // 2
        had = count_have(arr, brr, mid)
        if had < k:
            right = mid
        else:
            left = mid + 1
            
    had = count_have(arr, brr, left)
    total = count_sum(arr, brr, left) + (k - had) * left
    
    print(total)
        
        
    
        
        
    
    
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        solve(n, k, arr, brr)