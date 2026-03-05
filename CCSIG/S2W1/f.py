def solve(n, k, arr, brr):
    if k == 1:
        print(arr[0])
    else:
        sum_arr = [0] * n
        sum_arr[0] = arr[0]
        max_brr = [0] * n
        max_brr[0] = brr[0]
        for i in range(1, n):
            sum_arr[i] = sum_arr[i-1] + arr[i]
            max_brr[i] = max(max_brr[i-1], brr[i])
        ans = 0
        for i in range(min(n, k)):
            ans = max(ans, sum_arr[i] + max_brr[i]*(k-(i+1)))
        print(ans)
            

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        solve(n, k, arr, brr)