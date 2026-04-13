def solve(n, arr):
    arr.sort(reverse=True)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            continue
        else:
            print(-1)
            return
    print(*arr)
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)