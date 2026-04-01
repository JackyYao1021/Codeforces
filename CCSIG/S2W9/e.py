if __name__ == "__main__":
    s = input().strip()
    n = len(s)
    pref = [0] * (n + 1)

    for i in range(1, n):
        pref[i + 1] = pref[i]
        if s[i] == s[i - 1]:
            pref[i + 1] += 1

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(pref[r] - pref[l])