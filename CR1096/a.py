def solve(x, y):
    if x % 2 == 1 and y % 2 == 1:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        solve(x, y)