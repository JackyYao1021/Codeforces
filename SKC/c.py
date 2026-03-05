def solve(n, arr):
    diff = [0] * (n-1)
    
    for i in range(n-1):
        diff[i] = arr[i+1] - arr[i]
    tmp = 0
    ans = 0 
    for a in diff:
        ans += abs(a)
    for i in range(n-2):
        a, b = diff[i], diff[i+1]
        tmp = max(tmp, abs(a) + abs(b) - abs(a + b))
    tmp = max(tmp, abs(diff[0]))
    tmp = max(tmp, abs(diff[-1]))
    return ans - tmp
     
    
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(n, arr))