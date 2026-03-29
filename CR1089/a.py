def solve(n):
    ans = [i for i in range(n, 0, -1)]
    print(*ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)