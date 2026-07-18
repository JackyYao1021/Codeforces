def solve():
    n, k, m = map(int, input().split())
    if k > m:
        print("NO")
        return
    ans = [1] * n
    ans[0] += m - k
    print("YES")
    print(*ans)    
        


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()