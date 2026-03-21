from heapq import heappush, heappop
def solve(n, k, arr, brr):
    def check(x):
        need = 0
        for i in range(n):
            need += max(0, arr[i] * x - brr[i])
            if need > k:
                return False
        return True


    l = 0
    r = 10**10
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    print(ans)

if __name__ == "__main__":
    
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    solve(n, k, arr, brr)