from collections import Counter
def solve(n, arr):
    counter = Counter(arr)
    ans = []
    keys = sorted(counter.keys())
    for idx, a in enumerate(arr):
        counter[a] -= 1
        total = n - idx - 1 - counter[a]
        less_than_a = 0
        for k in keys:
            if k < a:
                less_than_a += counter[k]
            else:
                break
        ans.append(max(total - less_than_a, less_than_a))
    
    print(*ans)
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)