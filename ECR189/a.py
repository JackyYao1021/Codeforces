def solve(x, y):
    z = 2 * x
    while z < y:
        if y % z != 0:
            print("YES")
            return
        z += x
    print("NO")
    return

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        solve(x, y)