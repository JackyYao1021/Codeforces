def solve():
    ans = []
    n = int(input())
    arr = list(map(int, input().split()))
    mn = arr[0]
    tmp = arr[0]
    ans.append(mn)
    for i in range(1, n):
        tmp += arr[i]
        mn = min(mn, tmp// (i + 1))
        ans.append(mn)
    print(*ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()