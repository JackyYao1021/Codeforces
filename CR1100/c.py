def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    find_pos = True
    idx = n - 1
    ans = []
    while idx >= 0:
        if arr[idx] > 0 and find_pos:
            ans.append(idx+1)
            find_pos = False
        elif arr[idx] < 0 and not find_pos:
            ans.append(idx+1)
            find_pos = True
        idx -= 1
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()