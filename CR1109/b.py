def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    anchor = 0
    cand = 0
    for i in range(0, n):
        anchor += i+1
        cand += arr[i]
        if cand < anchor:
            print("NO")
            return
    print("YES")
    
        
        
        
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()