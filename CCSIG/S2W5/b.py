def solve(n, k):
    if n % 2 != k % 2:
        print("NO")
        return
    
    mn = ((1 + (2*k-1)) * k) // 2
    
    if n >= mn:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        solve(n, k)