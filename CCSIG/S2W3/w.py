def solve(n, arr):
    if n <= 2:
        print(-1)
        return 
    
    arr.sort()
    mid = arr[n//2]
    total = sum(arr)
    if total > 2 * mid * n:
        print(0)
        return
    else:
        print(2 * mid * n - total + 1)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)