def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    left = 0
    right = n - 1
    for left in range(n):
        if arr[left] == 1 or arr[left] == -1:
            break

    for right in range(n - 1, -1, -1):
        if arr[right] == 1 or arr[right] == -1:
            break
    
    ans = [0] * n
    for i in range(n):
        if arr[i] == -1:
            if i == left or i == right:
                ans[i] = 1
            else:
                ans[i] = 0
        else:
            ans[i] = arr[i]
    print(*ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()