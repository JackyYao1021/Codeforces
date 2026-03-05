from math import log2, ceil
def solve(n, arr):
    ans = 0
    for i in range(n-1):
        left = arr[i]
        right = arr[i+1]
        
        left, right = min(left, right), max(left, right)
        
        if right > 2 * left:
            # left * 2 ^ (x+1) > right 
            ans += ceil(log2(right / left)) - 1
        
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)