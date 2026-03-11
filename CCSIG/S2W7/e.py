from math import gcd

def solve(n, arr):
    arr.sort(key=lambda x: x % 2)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(arr[i], 2 * arr[j]) > 1:
                ans += 1
    print(ans)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)