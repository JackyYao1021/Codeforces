from heapq import heappush, heappop

def solve(n, m, l, arr):
    num = min(m-1, n)
    total = 0    
    prev = 0
    if num == m-1:
        arr = arr[n-m-1:]

    for i in range(num):
        total += arr[i]
        rem = total % num
        base = total // num
        mx = base
        if rem > 0:
            mx = base + 1
        
        total -= mx
        num -= 1
    ans = total + l - arr[-1]
    print(ans)

    
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, l = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, m, l, arr)
    
    
    