from collections import defaultdict
def helper(brr, diff):
    keys = sorted(k for k in brr.keys() if brr[k] > 0)
    tmp = brr[keys[0]]
    prev = keys[0]
    need = 0
    for key in keys[1:]:
        need = (key - prev) * tmp
        if need < diff:
            diff -= need
            tmp += brr[key]
            brr.pop(key)
        elif need == diff:
            brr[key] += tmp
            brr[key] -= 1
            if brr[key] == 0:
                brr.pop(key)
            return brr, key
        else:
            real_diff = diff // tmp
            rem = diff % tmp
            brr[prev+real_diff+1] += rem - 1
            brr[prev+real_diff] += tmp - rem
            if brr[prev+real_diff+1] == 0:
                brr.pop(prev+real_diff+1)
                return brr, prev+real_diff
            else:
                return brr, prev+real_diff+1
            
    real_diff = diff // tmp
    rem = diff % tmp
    brr[prev+real_diff+1] += rem - 1
    brr[prev+real_diff] += tmp - rem
    if brr[prev+real_diff+1] == 0:
        brr.pop(prev+real_diff+1)
        return brr, prev+real_diff
    else:
        return brr, prev+real_diff+1
            

def solve(n, m, l, arr):
    count = defaultdict(int)
    count[0] = n+1
    
    for i in range(n):
        diff = arr[i] - (arr[i-1] if i > 0 else 0)
        count, mx = helper(count, diff)
        
    diff = l - arr[-1]
    ans = mx + diff
    print(ans)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, l = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, m, l, arr)