def solve(n, arr):
    mx = 0
    tmp = 1
    
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            tmp += 1
        else:
            mx = max(mx, tmp)
            tmp = 1
    mx = max(mx, tmp)
            
    if mx > m-1:
        print("NO")
    else:
        print("YES")
    return 
        
        
        


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, arr)