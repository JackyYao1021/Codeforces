from collections import Counter
def solve(n, x, y, arr):
    brr = [(a % x, a % y) for a in arr]
    
    counter = Counter(brr)
    keys = list(counter.keys())
    ans = 0
    for key in keys:
        if (key[0]*2) % x == 0:
            ans += counter[key] * (counter[key]-1)
        else:
            key2 = (x-key[0], key[1])
            ans += counter[key] * counter.get(key2, 0)
    return ans // 2
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x, y = map(int, input().split())
        arr = list(map(int, input().split()))
        print(solve(n, x, y, arr))