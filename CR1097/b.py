from collections import Counter

def solve(n, arr):    
    counter = Counter(arr)
    keys = list(counter.keys())
    keys.sort()
    ans = n * keys[-1] # all max
    mex = 0
    for key in keys:
        if mex == key:
            mex += 1
        ans += mex
    if mex == keys[-1] + 1:
        ans -= keys[-1]
    else:
        ans -= mex
    
    ans += mex * (n - len(keys))
    print(ans)
        
    
        
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)
    
    