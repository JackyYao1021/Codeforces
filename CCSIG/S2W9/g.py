def solve(n):
    if n % 2 == 0:
        ans = n // 2
    else:
        ans = n // 2 - n
    print(ans)

if __name__ == "__main__":
    n = int(input())
    solve(n)