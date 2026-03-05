from collections import deque
def solve(n, arr, t):
    # from zero to t-1
    pos = 0
    while True:
        if pos >= t:
            print("NO")
            return
        if pos == t-1:
            print("YES")
            return
        pos += arr[pos]


if __name__ == "__main__":
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    solve(n, arr, t)