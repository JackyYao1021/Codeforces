def solve(n, k, arr):
    sorted_arr = sorted(arr)
    pre = sorted_arr[0]
    cnt = 1
    mx = 0
    for a in sorted_arr[1:]:
        if a - pre <= k:
           cnt += 1  
        else:
            mx = max(mx, cnt)
            cnt = 1
        pre = a
    mx = max(mx, cnt)
    print(n - mx)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, k, arr)