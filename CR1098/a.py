def solve(n, arr):
    cnt = [0, 0, 0]
    for a in arr:
        cnt[a % 3] += 1
    
    ans = cnt[0] + min(cnt[1], cnt[2])
    if cnt[1] > cnt[2]:
        ans += (cnt[1] - cnt[2]) // 3
    if cnt[2] > cnt[1]:
        ans += (cnt[2] - cnt[1]) // 3
    print(ans)
    
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)