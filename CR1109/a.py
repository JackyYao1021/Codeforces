def solve():
    n = int(input())
    s = input().strip()
    tmp = 0
    pre = False
    mx = 0
    for i in range(n):
        if s[i] == "#":
            tmp += 1
            pre = True
        else:
            pre = False
            mx = max(mx, tmp)
            tmp = 0
    mx = max(mx, tmp)
    print((mx+1) // 2)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()