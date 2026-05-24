def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    mn = min(arr)
    mx = max(arr)
    mid = (mn + mx) // 2
    print(max(mid - mn, mx - mid))
    
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()