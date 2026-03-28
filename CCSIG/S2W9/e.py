if __name__ == "__main__":
    s = input()
    n = len(s)
    
    prefix = [0] * (n + 2)    
    prefix[1] = 1
    for i in range(1, n):
        if s[i-1] == s[i]:
            prefix[i+1] = prefix[i] + 1
        else:
            prefix[i+1] = 1
        
    q = int(input())
    print(prefix)
    for _ in range(q):
        found = False
        l, r = map(int, input().split())
        for i in range(l, r+1):
            if prefix[i] == 1:
                print(max(max(prefix[i:r+2]), prefix[i-1] - prefix[l] + 1) - 1)
                found = True
                break
        if not found:
            print(r - l)
                
        
    

        
        
        