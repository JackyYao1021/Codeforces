from bisect import bisect_left
def solve(n, q, arr):
    
    arr.sort()
    sugar = [0] * n
    sugar[0] = arr[-1]
    for i in range(1, n):
        sugar[i] = sugar[i-1] + arr[n-i-1]
    
    for _ in range(q):
        target = int(input())
        
        idx = bisect_left(sugar, target)
        if idx == n:
            print(-1)
        else:
            print(idx+1)     


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, q, arr)
            
        