from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    keys = list(counter.keys())
    keys.sort()
    tmp = 0
    ans = float("inf")
    for key in keys:
        left = tmp
        right = n - left - counter[key]
        tmp_ans = min(left, right) + abs(left - right)
        ans = min(ans, tmp_ans)
        tmp += counter[key]
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()