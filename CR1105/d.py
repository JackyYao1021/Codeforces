def solve():
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    
    prefix_sum = [0] * (3*n+1)
    for i in range(3*n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i % n]
        
    ans = 0
    for i in range(n):
        diff = 2 * d * arr[i] - (prefix_sum[i+d+1+n] - prefix_sum[i-d+n] - arr[i])
        if diff > 0:
            ans += diff
    print(ans)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()