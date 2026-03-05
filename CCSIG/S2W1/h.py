def solve(n, arr):
    if n <= 2:
        print(0)
        return
    
    a = 10**9 + 1
    b = 10**9 + 1
    ans = 0
    for i in range(n):
        c = arr[i]
        if c <= a:
            a, b = c, b
        elif c <= b:
            b = c
        else:
            ans += 1
            a, b = b, c
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)