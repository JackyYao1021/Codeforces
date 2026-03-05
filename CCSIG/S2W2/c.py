def solve(n, arr):
    pre = '#'
    tmp = 0
    cnt = 0
    mx = 0
    for a in arr:
        if a == '#':
            pre = '#'
            mx = max(mx, tmp)
            tmp = 0  
            continue
        if a == '.':
            cnt += 1 
            tmp += 1
    mx = max(mx, tmp)
                
    if mx >= 3:
        print(2)
        return
    print(cnt)
    
        
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(input().strip())
        solve(n, arr)