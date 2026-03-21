from heapq import heappush, heappop
def solve(n, m, arr):
    spaces = []
    arr.sort()
    prev = arr[0]
    for i in range(1, m):
        heappush(spaces, -(arr[i] - prev - 1))
        prev = arr[i]
        
    heappush(spaces, -(n - arr[-1] + arr[0] - 1))

    ans = 0
    step = 0
    while spaces:
        space = - heappop(spaces)
        if space == step + 1:
            ans += 1
            break
        elif space > step + 1:
            ans += space -step-1
        else:
            break
        
        step += 4
            
    print(n - ans)
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, m, arr)