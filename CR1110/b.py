def solve():
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for i in range(n):
        arr[i] = arr[i] - c
    
    arr.sort(reverse=True)
    l = len(arr)
    ans = 0
    
    for i in range((l+1)//2):
        ans += arr[i]
    for i in range((l+1)//2, l):
        if arr[i] > 0:
            ans += arr[i]
    print(ans)
                



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()