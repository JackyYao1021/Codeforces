def solve(n, arr):
    ans = []
    total = 0
    sm = (arr[0] + arr[-1]) // (n-1)
    for i in range(1, n):
        diff = arr[i-1] - arr[i]
        x = (sm - diff - 2* total) // 2 
        ans.append(x)
        total += x
    
    ans.append(sm - total)
    print(" ".join(map(str, ans)))



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)