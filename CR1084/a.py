def solve(n, arr):
    mx = max(arr)
    ans = 0
    for a in arr:
        if a == mx:
            ans += 1
            
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)