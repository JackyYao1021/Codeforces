def solve(arr):
    minus_one = arr.count(-1)
    zero = arr.count(0)
    return 2 * (minus_one % 2) + zero


t= int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))