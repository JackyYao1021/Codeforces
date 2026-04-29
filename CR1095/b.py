def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(n, arr):
    ans = 0
    for i in range(n-1):
        a, b = arr[i], arr[i+1]
        diff = abs(a - b)
        if diff == gcd(a, b):
            ans += 1
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)
        