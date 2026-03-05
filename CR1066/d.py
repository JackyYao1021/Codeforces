def solve(l, r, estimates):
    ans = 0
    left = []
    right = []
    middle = []
    l_val = 0
    r_val = 0    
    for estimate in estimates:
        if estimate < l:
            l_val += l - estimate
            r_val += r - estimate
        elif estimate > r:
            l_val += estimate - l
            r_val += estimate - r
        else:
            middle.append(estimate)

    # diff_val = abs(l_val - r_val)
    # diff = r - l + 1
        
    if middle:
        n = len(middle)
        middle.sort()
        prefix = [0] * (len(middle)+1) 
        for i in range(1, len(middle)+1): 
            prefix[i] = prefix[i-1] + middle[i-1]
        
        surffix = [0] * (len(middle)+1)   
        for i in range(len(middle)-1, -1, -1):
            surffix[i] = surffix[i+1] + middle[i]
            
        for i in range(len(middle)):
            ans = max(ans, min(l_val - (prefix[i] - i*l) + (surffix[i] - (n-i)*l), r_val + (i*r - prefix[i]) - ((n-i)*r - surffix[i])))
            ans = max(ans, min(l_val - (prefix[i] - i*l) + (surffix[i+1] - (n-i-1)*l), r_val + (i*r - prefix[i]) - ((n-i-1)*r - surffix[i+1])))
        ans = max(ans, min(l_val - (prefix[n] - n*l), r_val + (n*r - prefix[n])))
        
        return ans
    else:
        return min(l_val, r_val)
        



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, l, r = map(int, input().split())
        estimates = map(int, input().split())
        print(solve(l, r, estimates))