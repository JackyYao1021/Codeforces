def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    mx = 0
    ans = 0
    for i in range(n):
        if brr[i] > arr[i]:
            ans += brr[i]
            mx = max(mx, arr[i])
        else:
            ans += arr[i]
            mx = max(mx, brr[i])
    print(ans + mx)
    
        

    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()