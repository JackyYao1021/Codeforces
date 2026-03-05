from collections import defaultdict
def solve(n, arr):

    arr_extended = [0] + arr
    a = [0] * (n + 1)
    
    next_new_value = 1
    
    for i in range(1, n + 1):
        p = i - (arr_extended[i] - arr_extended[i-1])
        if p == 0:
            a[i] = next_new_value
            next_new_value += 1
        else:
            a[i] = a[p]
    return a[1:]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(*solve(n, arr))