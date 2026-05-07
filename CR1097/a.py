def solve(n, arr):
    cnt = 0
    if arr[-1] > 0:
        cnt += 1
    for i in range(n-2, -1, -1):
        if arr[i+1] > 0:
            arr[i] = arr[i] + arr[i+1] 
        if arr[i] > 0:
            cnt += 1
    print(cnt)  
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t): 
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)