def solve(n, m):
    a = 0
    b = 0
    for i in range(200):
        a *= 10
        a += 9
    for i in range(200):
        a *= 10
        b *= 10
        b += 9
    a += 1
    print(a)
    print(b)



if __name__ == "__main__":
    n, m = map(int, input().split())
    solve(n, m)