t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    a_s = list(map(int, input().split()))
    b_s = list(map(int, input().split()))
    ans = 0
    for a in a_s:
        if a <= y and a >= 0:
            ans += 1
    for b in b_s:
        if b <= x and b >= 0:
            ans += 1
    print(ans)