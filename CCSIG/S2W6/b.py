def solve(xa, ya, xb, yb):
    if yb < ya:
        print("-1")
        return
    
    new_x = xa + yb - ya
    if new_x < xb:
        print("-1")
        return

    print(yb - ya + new_x - xb)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        xa, ya, xb, yb = map(int, input().split())
        solve(xa, ya, xb, yb)