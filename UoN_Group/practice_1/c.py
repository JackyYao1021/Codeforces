def solve():
    ans = 0
    for i in range(10):
        s = input()
        for j, c in enumerate(s):
            if c == 'X':
                ans += min(i+1, 10-i, j+1, 10-j)
    print(ans)
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
