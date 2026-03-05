def solve(arr):
    mx = max(arr[0], arr[1])
    ans = 0
    for i in range(1, len(arr), 2):
        mx = max(mx, arr[i-1], arr[i])
        arr[i] = mx
        
    ans = max(arr[0] - arr[1] + 1, 0)
    
    for i in range(2, len(arr), 2):
        diff_1 = 0
        diff_2 = 0
        if arr[i] >= arr[i-1]:
            diff_1 = arr[i] - arr[i-1] + 1
        if i < len(arr) - 1 and arr[i] >= arr[i+1]:
            diff_2 = arr[i] - arr[i+1] + 1
        ans += max(diff_1, diff_2)
        
        
    return ans

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))