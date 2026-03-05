from collections import Counter
t = int(input())
for _ in range(t):
    ans = 0
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    counter = Counter(l)
    dic = {}
    for key, value in counter.items():
        if value % k != 0:
            print(0)
            break
        else:
            dic[key] = value // k
    count = Counter()
    left = 0    
    for right in range(n):
        count[l[right]] += 1

        while l[right] in dic and count[l[right]] > dic[l[right]]:
            count[l[left]] -= 1
            left += 1

        ans += right - left + 1
    print(ans)