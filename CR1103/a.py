def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    mn = min(arr)
    print(mx - mn + 1)




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()