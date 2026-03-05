def solve(x, y, z, d, ms, n, m, k):
    for m in ms:
        
    
    
    # total = 0
    # for i in range(n):
    #     need = y[i] - x[i]
    #     if need <= 0:
    #         continue
    #     if d[i] <= 0:
    #         return -1
    #     cnt = (need + d[i] - 1) // d[i]
    #     total += cnt
    # if total > k:
    #     return -1
    # rem = k - total
    # ms.sort()
    # idx = 0
    # while rem > 0 and idx < m:
    #     rem -= ms[idx]
    #     total += 1
    #     idx += 1
    # if rem > 0:
    #     return -1
    # return total
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        ms = list(map(int, input().split()))
        x, y, z = [], [], []
        for _ in range(n):
            a, b, c = map(int, input().split())
            x.append(a)
            y.append(b)
            z.append(c)
        d = [z[i] - y[i] for i in range(n)]
        print(solve())