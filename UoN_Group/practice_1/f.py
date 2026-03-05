from math import sqrt
def solve(n, c, arr):
    inner_square = 0
    sum_a = 0
    for a in arr:
        inner_square += a * a
        sum_a += a
    C = c-inner_square
    ans = (sqrt(sum_a**2 + n*C) - sum_a) // (2*n)
    return int(ans)
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, c = map(int, input().split())
        arr = list(map(int, input().split()))
        print(solve(n, c, arr))