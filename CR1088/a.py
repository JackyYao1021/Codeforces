def solve(n, arr):
    ans = []
    if n == 1:
        ans.append(1)
        print(*ans)
        return
        
    ans = [2] * n
    print(*ans)
        
    
        
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)