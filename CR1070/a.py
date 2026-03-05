def solve(arr):
    mx = arr[0]
    ans = 0
    for a in arr:
        if a >= mx:
            mx = a
        else:
            ans += 1
    return ans

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))
    