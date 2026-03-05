from collections import defaultdict
from bisect import bisect_left, bisect_right
def solve(s, t, k):
    if s[0] != t[0]:
        return -1
    dic = defaultdict(list)
    dic[s[0]].append(0)
    mx = 0
    for i in range(1, len(s)):
        dic[s[i]].append(i)
        if t[i] not in dic:
            return -1
        else:
            idx = bisect_right(dic[t[i]], i - mx) - 1 
            if idx == -1:
                return -1
            mx = max(mx, i - dic[t[i]][idx])
    return mx


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        t = input()
        print(solve(s, t, k))