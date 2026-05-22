def solve(n, x1, x2, k):
    if n <= 3:
        print(1)
        return 
    diff = abs(x1 - x2)
    if diff > n - diff:
        diff = n - diff
    print(diff + k)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x1, x2, k = map(int, input().split())
        solve(n, x1, x2, k)