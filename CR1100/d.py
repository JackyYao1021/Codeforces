def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    
    def check(k):
        stack = []
        for i in range(n):
            if arr[i] >= k and brr[i] >= k:
                stack.append(1)
            elif arr[i] < k and brr[i] < k:
                stack.append(0)

        if not stack:
            return False
        
        merged = [stack[0]]
        for i in range(1, len(stack)):
            if stack[i] == 0 and merged[-1] == 0:
                continue
            merged.append(stack[i])
                
        return merged.count(1) > merged.count(0)
    
    l = 1
    r = 2*n+1
    ans = 1
    
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()