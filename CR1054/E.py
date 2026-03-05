from collections import defaultdict

def count_at_most(arr, K, maxlen):
    if K < 0 or maxlen <= 0:
        return 0
    n = len(arr)
    freq = defaultdict(int)
    left = 0
    distinct = 0
    res = 0

    for right, x in enumerate(arr):
        if freq[x] == 0:
            distinct += 1
        freq[x] += 1
        
        while distinct > K:
            y = arr[left]
            freq[y] -= 1
            if freq[y] == 0:
                distinct -= 1
            left += 1

        while right - left + 1 > maxlen:
            y = arr[left]
            freq[y] -= 1
            if freq[y] == 0:
                distinct -= 1
            left += 1

        res += (right - left + 1)

    return res

def solve(n, k, l, r, arr):
    return (count_at_most(arr, k, r) - count_at_most(arr, k, l-1)
          - (count_at_most(arr, k-1, r) - count_at_most(arr, k-1, l-1)))

t = int(input())
for _ in range(t):
    n, k, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, l, r, arr))
