from collections import Counter
t = int(input())


def solve(arr):
    cnt = Counter(arr)
    if cnt[0] == 1:
        idx = arr.index(0)
        if (idx+1) not in arr:
            arr[arr.index(0)] = idx + 1
        else:
            arr[arr.index(0)] = -1
    left, right = -1, -1
    for i in range(1, len(arr)+1):
        if arr[i-1] != i:
            left = i
            break
    for i in range(len(arr), 0, -1):
        if arr[i-1] != i:
            right = i
            break
    if left == right:
        return 0
    return right - left + 1

for _ in range(t):
    n = int(input())
    arrs = list(map(int, input().split()))
    print(solve(arrs))