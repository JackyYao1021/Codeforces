def solve(n, c, k, arr):
    arr.sort()
    for a in arr:
        if a > c:
            print(c)
            return
        else:
            new_a = min(c, a+k)
            diff = new_a - a
            k -= diff
            c += new_a
    print(c)
    return 
            
            
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, c, k = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, c, k, arr)