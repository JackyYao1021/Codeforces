def solve(n, k, queries):
    queries.sort()
    ans = [-1] * n
    
    diff1 = [0] * (n + 1)
    diff2 = [0] * (n + 1)
    for q, l, r in queries:
        if q == 1:
            diff1[l - 1] += 1
            diff1[r] -= 1
        else:
            diff2[l - 1] += 1
            diff2[r] -= 1
        
    cover1 = 0
    cover2 = 0    
    num = 0
    for i in range(n):
        cover1 += diff1[i]
        cover2 += diff2[i]
        
        if cover1 > 0 and cover2 > 0:
            ans[i] = k+1
        elif cover1 > 0:
            ans[i] = k
        else:
            ans[i] = num
            num = (num + 1) % k

    return ans
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        queries = []
        for _ in range(q):
            queries.append(tuple(map(int, input().split())))
        print(*solve(n, k, queries))