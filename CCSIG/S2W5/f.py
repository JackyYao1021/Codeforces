def solve(zero, one, two):
    ans = []
    
    if zero == 0 and one == 0:
        for i in range(two+1):
            ans.append(1)
        print("".join(map(str, ans)))
        return
    if one == 0 and two == 0:
        for i in range(zero+1):
            ans.append(0)
        print("".join(map(str, ans)))
        return
    
    for i in range(zero+1):
        ans.append(0)
    
    for i in range(1, one, 2):
        ans.append(1)
        ans.append(0)
    
    if one % 2 == 1:
        ans.append(1)
        
    tmp = ans[-1]
    ans.pop(-1)
    
    for i in range(two):
        ans.append(1)
    
    ans.append(tmp)
    print("".join(map(str, ans)))
        
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        zero, one, two = map(int, input().strip().split())
        solve(zero, one, two)