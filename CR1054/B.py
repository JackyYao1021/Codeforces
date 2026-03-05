def solve(arr):
    ans = 0
    arr.sort()
    for i in range(len(arr)//2):
        ans = max(abs(arr[2*i+1] - arr[2*i]), ans)
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))