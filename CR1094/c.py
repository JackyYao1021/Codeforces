def check(arr, n):
    
    


def solve(n, arr):
    l = 1
    r = n
    while l < r:
        mid == (l+r) // 2 
        if check(arr, mid):
            l = mid + 1
        else:
            r = mid
    return l - 1
           

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve = solve(n, arr)