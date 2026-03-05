def solve(n, k, s):
    arr = list(s)
    ans = 0
    left = 0
    while left < n:
        if arr[left] == 'B':
            for i in range(left, min(left + k, n)):
                arr[i] = 'W'
            ans += 1
            left += k
        else:
            left += 1

    return ans

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        print(solve(n, k, s))