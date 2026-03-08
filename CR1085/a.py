def solve(n, s):
    left = 0
    mx_ans = 0
    mn_ans = 0

    while left < n and s[left] == "0":
        left += 1

    if left == n:
        print(0, 0)
        return

    right = left + 1

    while left < n:
        while left < n and s[left] == "0":
            left += 1

        if left >= n:
            break

        right = left + 1

        while right < n:
            if s[right] == "1":
                right += 1
            else:
                if right + 1 < n and s[right - 1] == "1" and s[right + 1] == "1":
                    right += 1
                else:
                    break

        length = right - left
        mx_ans += length
        if length > 2:
            if length % 2 == 0:
                mn_ans += length - ((length - 2) // 2)
            else:
                mn_ans += length - ((length - 1) // 2)
        else:
            mn_ans += length

        left = right + 1

    print(mn_ans, mx_ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        solve(n, s)