def solve(n, arr):
    if n > 2:
        print("NO")
        return
    
    diff = arr[1] - arr[0]
    
    if diff >= 2:
        print("YES")
        return 
    print("NO")
    
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)