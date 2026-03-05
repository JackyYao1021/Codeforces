def solve(n, x, arr):
    mx = 0
    pre = 0
    for a in arr:
        mx = max(a - pre, mx)
        pre = a
    mx = max(2 * (x - pre), mx) 
    
    print(mx)       
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x  = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, x, arr)