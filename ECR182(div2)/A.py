t = int(input())

def solve(arr):
    n = len(arrs)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = (prefix_sum[i] + arrs[i]) % 3

    for l in range(1, n-1):
        for r in range(l + 1, n):
            s1 = prefix_sum[l] % 3
            s2 = (prefix_sum[r] - prefix_sum[l]) % 3
            s3 = (prefix_sum[n] - prefix_sum[r]) % 3        
            if s1 == s2 and s2 == s3:
                return f"{l} {r}"
            if s1 != s2 and s2 != s3 and s1 != s3:
                return f"{l} {r}"
    return "0 0"


for _ in range(t):
    n = int(input())
    arrs = list(map(int, input().split()))
    print(solve(arrs))