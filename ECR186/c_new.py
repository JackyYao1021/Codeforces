def count_good_shifts(x, y):
    """count d in [0,n) such that for all i: x[i] < y[(i+d)%n]"""
    n = len(x)
    good = 0
    for d in range(n):
        ok = True
        for i in range(n):
            if x[i] >= y[(i + d) % n]:
                ok = False
                break
        if ok:
            good += 1
    return good

def solve(a, b, c):
    n = len(a)
    kab = count_good_shifts(a, b)
    kbc = count_good_shifts(b, c)
    return n * kab * kbc

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        print(solve(a, b, c))
