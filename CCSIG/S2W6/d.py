def solve(n, c, s):
    ans = 0
    left = 0
    right = 0
    
    if c == 'g':
        print("0")
        return
    while left < n:
        if s[left] == c:
            right = left
            while s[right] != 'g':
                right = (right + 1) % n
            if right < left:
                ans = max(ans, right + n - left)
                print(ans)
                return
            else:
                ans = max(ans, right - left)
                left = right
        left += 1
        
    print(ans)
        
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, c = input().split()
        n = int(n)
        s = input()
        solve(n, c, s)