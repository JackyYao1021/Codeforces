def solve(n, s):
    symbol_count = set()
    pre_sum = [0] * n
    pre_sum[0] = 1
    idx = 1
    symbol_count.add(s[0])
    while idx < n:
        char = s[idx]
        if char not in symbol_count:
            symbol_count.add(char)
            pre_sum[idx] = pre_sum[idx-1] + 1
        else:
            pre_sum[idx] = pre_sum[idx-1]
        idx += 1
        
        
    suff_sum = [0] * n   
    suff_sum[n-1] = 1
    symbol_count = set()
    symbol_count.add(s[-1])
    
    idx = n-2
    while idx >= 0:
        char = s[idx]
        if char not in symbol_count:
            symbol_count.add(char)
            suff_sum[idx] = suff_sum[idx+1] + 1
        else:
            suff_sum[idx] = suff_sum[idx+1]
        idx -= 1
        
    mx = 0
    for i in range(0, n-1):
        mx = max(mx, pre_sum[i] + suff_sum[i+1])
        
    print(mx)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        solve(n, s)