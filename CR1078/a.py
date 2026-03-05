def solve(n, w):
    print(n - (n//w))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, w = map(int, input().split())
        solve(n, w)