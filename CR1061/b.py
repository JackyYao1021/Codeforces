def solve(n, q, s_list, arr):
    n = len(s_list)
    if len(s_list) == 1:
        l, m = s_list[0]
        for a in arr:
            if m == 0:
                print(a)
            else:
                print(a.bit_length())
        return
    
    for a in arr:
        idx = 0
        time = 0
        while a:
            l, m = s_list[idx]
            if m == 0:
                take = min(l, a)
                time += take
                a -= take
            else:
                take = min(l, a.bit_length())
                time += take
                a >>= take
            idx = (idx + 1) % n
        print(time)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        s = input()
        s_list = []
        i = 0
        while i < n:
            l = 1
            while i + l < n and s[i + l] == s[i]:
                l += 1
            s_list.append((l, 0 if s[i] == 'A' else 1))
            i += l

        arr = list(map(int, input().split()))
        solve(n, q, s_list, arr)