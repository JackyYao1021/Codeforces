def solve(n, x, y, arr):
    total = sum(a // x for a in arr)
    ans = 0
    for a in arr:
        ans = max(ans, a + y * (total - a // x))
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x, y = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, x, y, arr)