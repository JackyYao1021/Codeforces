from collections import defaultdict
def solve(n, xrr, trr):
    mx_sum = 0
    mx_diff = -float('inf')
    for x, t in zip(xrr, trr):
        mx_sum = max(mx_sum, x + t)
        mx_diff = max(mx_diff, t - x)

    print((mx_sum - mx_diff) / 2)
        
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        xrr = list(map(int, input().split()))
        trr = list(map(int, input().split()))
        solve(n, xrr, trr)