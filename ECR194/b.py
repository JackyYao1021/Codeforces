def solve():
    x, y, k = map(int, input().split())
    ans = 0
    delta = y - x
    
    diff_cnt = min(k, max(0, delta - x + 1))

    for i in range(diff_cnt):
        ans += delta % (x + i)
    ans += (k - diff_cnt) * delta
    
    print(ans)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()