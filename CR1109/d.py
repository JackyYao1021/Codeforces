def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    
    distinct_idx = set(brr)
    sorted_idx = sorted(distinct_idx)
    l = 0
    ans = 0
    for r in sorted_idx:
        ans += abs(prefix_sum[r] - prefix_sum[l])
        l = r
    
    ans += prefix_sum[n] - prefix_sum[l]
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()