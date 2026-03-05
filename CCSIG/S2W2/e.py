from math import sqrt
def solve(y, brr):
    ans = [0] * n
    sorted_brr = sorted(brr)
    idx = 0
    for i in range(n-1):        
        ans[i] = sorted_brr[idx]
        idx += n-1-i
    ans[-1] = ans[-2]
    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        brr = list(map(int, input().split()))
        solve(n, brr)