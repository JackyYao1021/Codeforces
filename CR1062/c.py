def solve(n, arr):
    num_odd = sum(1 for x in arr if x % 2 != 0)
    if num_odd == n or num_odd == 0:
        return arr
    else:
        arr.sort()
        return arr



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(*solve(n, arr))