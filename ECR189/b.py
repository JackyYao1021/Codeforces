def solve(s):
    left = 0
    right = len(s) - 1 
    
    while left < right:
        if s[left] == s[left+1]:
            break
        left += 1
    
    while right > left:
        if s[right] == s[right-1]:
            break
        right -= 1
        
    if left == right:
        print("YES")
        return
    for i in range(left+1, right-1):
        if s[i] == s[i+1]:
            print("NO")
            return
    print("YES")
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip()
        solve(s)