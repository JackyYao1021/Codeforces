def solve(n, r, x1, y1, x2, y2, x3, y3, x4, y4):
    long = 0
    high = 0
    long = max(long, abs(x1-x2), abs(x1-x3), abs(x1-x4), abs(x2-x3), abs(x2-x4), abs(x3-x4))
    high = max(high, abs(y1-y2), abs(y1-y3), abs(y1-y4), abs(y2-y3), abs(y2-y4), abs(y3-y4))

    left_down_x = min(x1, x2, x3, x4)
    left_down_y = min(y1, y2, y3, y4)

    a = (long - r) // 2 + 2
    b = high // (sqrt(3) * r)
    
    print((2*a+1) * b)
    for i in range(b):
        for j in range(a):
            print(left_down_x + j* 2 *r, left_down_y + floor(i* 2 *sqrt(3)*r))

if __name__ == "__main__":
    n, r = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    solve(n, r, x1, y1, x2, y2, x3, y3, x4, y4)