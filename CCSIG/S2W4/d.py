from collections import Counter
def solve(n, arr):
    counter = Counter(arr)
    for key, value in counter.items():
        if value == 1:
            print(-1)
            return
    
    left = 0
    right = 1
    ans = [1] * n
    while right < n:
        while right < n and arr[left] == arr[right]:
            right += 1
        for i in range(left, right-1):
            ans[i] += i+1
        ans[right-1] += left
        left = right
    for i in range(left, right-1):
        ans[i] += i+1
        ans[right-1] += left
    print(" ".join(map(str, ans)))
        
         
    




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)