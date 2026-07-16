def solve():
    n, k = map(int, input().split())
    s = input().strip()
    l = len(s)
    if 2 * k > l:
        print(-1)
        return
    ans = 0
    for i in range(k):
        if s[i] == "L":
            ans += 1
    for i in range(l-1, l-k-1, -1):
        if s[i] == "R":
            ans += 1
    print(ans)
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()