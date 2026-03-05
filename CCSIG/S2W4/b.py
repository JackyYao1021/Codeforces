def solve(x):
    x = abs(x)
    n = 1
    s = 0
    while s < x or (s - x) % 2 == 1:
        s += n
        n += 1
    print(n-1)



if __name__ == "__main__":
    x = int(input())
    solve(x)