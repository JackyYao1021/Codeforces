def solve(x, y):
    if x < y:
        return 2
    if (x-1) > y and y > 1:
        return 3
    return -1


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(solve(x, y))