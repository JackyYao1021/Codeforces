def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 2
    if arr.count(0) < 2:
        print(-1)
        return 
    else:
        if arr[0] == 0:
            ans -= 1
        if arr[-1] == 0:
            ans -= 1
    print(ans)
    
            
        



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        