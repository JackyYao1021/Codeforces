def solve(n, q, arr, brr, queries):
    tmp = [0] * (n)
    tmp[-1] = max(arr[-1], brr[-1])
    for i in range(n-2, -1, -1):
        tmp[i] = max(tmp[i+1], arr[i], brr[i])
    ans = []
    prefix = [0] * (n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + tmp[i-1]
        
    
    
    for l, r in queries:
        ans.append(prefix[r] - prefix[l-1])
    print(*ans)
        
        


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        
        queries = []
        for _ in range(q):
            l, r = map(int, input().split())
            queries.append((l, r))
        solve(n, q, arr, brr, queries)