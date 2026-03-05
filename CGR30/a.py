def solve(n, arr, x):
    mx = max(arr)
    mn = min(arr)
    if mn <= x <= mx:
        return "YES"
    return "NO"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        x = int(input())
        print(solve(n, arr, x))
    
    