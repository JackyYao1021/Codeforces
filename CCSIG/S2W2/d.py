def solve(n, arr):
    tmp = 1
    mx = 0
    diff_list = []
    pre = arr[0]
    for a in arr[1:]:
        if a == pre:
            tmp += 1
        else:
            diff_list.append(tmp)
            mx = max(mx, tmp)
            tmp = 1
            pre = a
        
    mx = max(mx, tmp)
    print(mx + 1)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(input().strip())
        solve(n, arr)