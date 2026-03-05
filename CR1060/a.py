def solve(n, s, k):
    ans = 0
    pre = -k-1
    for i in range(0, n):
        if s[i] == '1':
            if i - pre >= k:
                ans += 1
            pre = i
    return ans
        
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        print(solve(n, s, k))
        