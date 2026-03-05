def solve(m, s):
    if s > 9 * m or s == 0 and m > 1:
        print("-1 -1")
        return
    if s == 0 and m == 1:
        print("0 0")
        return
    
    mx = [0] * m
    mn = [0] * m
    
    s_mx = s
    for i in range(m):
        if s_mx > 9:
            mx[i] = 9
            s_mx -= 9
        else:
            mx[i] = s_mx
            s_mx = 0
        
    s_mn = s - 1   
    mn[0] = 1
    
    if s_mn > 0:
        for i in range(m-1, -1, -1):
            if s_mn > 9:
                mn[i] += 9
                s_mn -= 9
            else:
                mn[i] += s_mn
                break
    print("".join(map(str, mn)), "".join(map(str, mx)))
        
        
         

if __name__ == "__main__":
    m, s = map(int, input().split())
    solve(m, s)