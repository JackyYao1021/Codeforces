from collections import defaultdict

def preprocess(arr):
    l = len(arr)
    length_set = set()
    length = [[] for _ in range(len(arr) + 1)]

    for i in range(len(arr)):
        seen = set()
        mn = float("inf")
        mx = -float("inf")

        for j in range(i, len(arr)):
            if j - i + 1 > l // 2:
                break
            if arr[j] in seen:
                break
            seen.add(arr[j])
            mn = min(mn, arr[j])
            mx = max(mx, arr[j])
            
            if mx - mn + 1 == j - i + 1:
                length[j - i + 1].append((i, mn))
                length_set.add(j - i + 1)

    return length, length_set


def check(length_list, seg_len):
    dic = {}
    for i in range(len(length_list)):
        idx, mn = length_list[i]
        if mn - seg_len in dic and dic[mn - seg_len] < idx - seg_len + 1:
            return True
        if mn + seg_len in dic and dic[mn + seg_len] < idx - seg_len + 1:
            return True
        if mn not in dic:
            dic[mn] = idx
         

    return False


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    length, length_set = preprocess(arr)
    length_set = sorted(length_set, reverse=True)
    ans = 0
    for seg_len in length_set:
        if check(length[seg_len], seg_len):
            ans = seg_len
            break
    print(ans)
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()