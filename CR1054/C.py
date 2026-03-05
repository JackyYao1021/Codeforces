def solve(n, k, arr):
    arr.sort()
    has_list = [1] * k
    cnt_K = 0
    for e in arr:
        if e > k:
            break
        if e == k:
            cnt_K += 1
        elif e < k:
            has_list[e] = 0
    return max(cnt_K, has_list.count(1))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))