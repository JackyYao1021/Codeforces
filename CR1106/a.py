from collections import Counter
def solve():
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    
    ans = float('inf')
    tmp = 0
    for i in range(n):
        if arr[i] >= brr[i]:
            tmp += arr[i] - brr[i]
        else:
            tmp = float('inf')
    ans = min(ans, tmp)
    
    arr.sort(reverse=True)
    brr.sort(reverse=True)
    idx = 0
    tmp = 0
    for b in brr:
        if arr[idx] >= b:
            tmp += arr[idx] - b
            idx += 1
        else:
            tmp = float('inf')
            break
    ans = min(ans, tmp+c)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()