def solve():
    n, q = map(int, input().split())
    s = input().strip()
    left_count = [0] * n
    right_count = [0] * n
    for i in range(1, n):
        if s[i] == s[i - 1]:
            left_count[i] = left_count[i - 1] + 1
        else:
            left_count[i] = left_count[i - 1]
    for i in range(n - 2, -1, -1):
        if s[i] == s[i + 1]:
            right_count[i] = right_count[i + 1] + 1
        else:
            right_count[i] = right_count[i + 1]
    
    ans = [0] * n
    
    for _ in range(q):
        l, r, k = map(int, input().split())
        l -= 1
        r -= 1
        
        cnt = left_count[r] - left_count[l] 
        if (cnt + 1) // 2 > k:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()