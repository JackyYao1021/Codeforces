def c1(n, arr):
    find_pos = True
    idx = n - 1
    ans = []
    while idx >= 0:
        if arr[idx] > 0 and find_pos:
            ans.append(idx+1)
            find_pos = False
        elif arr[idx] < 0 and not find_pos:
            ans.append(idx+1)
            find_pos = True
        idx -= 1
    return ans 

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    prefix_sum = [0] * (n+1)
    mx = sum(arr)
    idx = -1
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + abs(arr[i])
    suffix_sum = [0] * n
    for i in range(n-2, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + arr[i+1]
    
    for i in range(n):
        if arr[i] > 0 and prefix_sum[i] - arr[i] + suffix_sum[i] > mx:
            mx = prefix_sum[i] - arr[i] + suffix_sum[i]
            idx = i
    # print(idx)
    # print(prefix_sum)
    # print(suffix_sum)
    ans = c1(idx, arr[:idx])
    if idx == -1:
        print(0)
        print()
    else:
        ans.append(idx+1)
        print(len(ans))
        print(*ans)
    
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()