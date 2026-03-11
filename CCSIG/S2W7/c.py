def solve(a):
    if a == 1:
        print(0)
        return
    if a % 3 != 0:
        print(-1)
    else:
        cnt_3 = 0
        while a % 3 == 0:
            a //= 3
            cnt_3 += 1
        cnt_2 = 0
        while a % 2 == 0:
            a //= 2
            cnt_2 += 1
        if a != 1 or cnt_3 < cnt_2:
            print(-1)
        else:
            ans = cnt_3 + cnt_3 - cnt_2
            print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        solve(a)