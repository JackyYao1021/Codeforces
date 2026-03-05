def solve(n, arr):
    cnt_odd = 0
    cnt_even = 0
    for a in arr:
        if a % 2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1
    
    if cnt_odd > 0 and cnt_odd % 2 == 0 and cnt_even != 0:
        print("YES")
        return 
    elif cnt_odd % 2 == 1:
        print("YES")
        return 
    
    print("NO")
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)