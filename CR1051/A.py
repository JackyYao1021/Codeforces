def solve():
    n = int(input())
    ps = list(map(int, input().split()))
    idx = ps.index(n)
    value = n
    left = idx
    right = idx
    while left > 0 or right < n - 1:
        value -= 1
        if (left > 0 and ps[left - 1] == value) or (right < n - 1 and ps[right + 1] == value):
            if left > 0 and ps[left - 1] == value:
                left -= 1
            else:
                right += 1
        else:
            return "NO"
    return "YES"
 
t = int(input())
for _ in range(t):
    print(solve())