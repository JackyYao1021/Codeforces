def solve():
    n, k = map(int, input().split())
    s = input().strip()
    ans = 0 
    for i in range(n // k):
        find_zero = False
        for j in range(k):
            if s[i*k + j] == "0":
                find_zero = True
                break
        if not find_zero:
            ans += 1
    print(ans)
            
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()