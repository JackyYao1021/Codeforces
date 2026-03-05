def solve(n):
    if n >= 5:
        return 5*n**2 - 5*n - 5
    if 2 < n < 5:
        return 4*n**2 - n - 4
    if n == 1:
        return 1
    if n == 2:
        return 9
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))