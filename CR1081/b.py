def solve(n, s):
    n1 = s.count('1')
    n0 = n - n1
    
    if n1 == 0:
        print(0)
        return 

    if n == 1:
        print(-1)
        return 
    
    if n0 == 1:
        print(1)
        for i in range(n):
            if s[i] == '0':
                print(i + 1)
                return    
    
    if n1 % 2 == 0:
        ans = []
        for i in range(n):
            if s[i] == '1':
                ans.append(i + 1)
        print(len(ans))
        if len(ans) > 0:
            print(*ans)
        return 
    
    if n0 % 2 == 1:
        ans = []
        for i in range(n):
            if s[i] == '0':
                ans.append(i + 1)
        print(len(ans))
        if len(ans) > 0:
            print(*ans)
        return 
    
    print(-1)
        
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):    
        n = int(input())
        s = input().strip()
        solve(n, s)
    