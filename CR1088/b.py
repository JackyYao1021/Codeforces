MOD = 676767677

def factors(n):
    result = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return result

def solve(a, b):
    if a < b:
        diff = b - a
        factors_diff = factors(diff)
        print(len(factors_diff) % MOD)
        print(*([1]*a + [-1]*b))
    elif a > b:
        diff = a - b
        factors_diff = factors(diff)
        print(len(factors_diff) % MOD)
        print(*([1]*a + [-1]*b))
    else:
        print(1)
        print(*([1]*a + [-1]*b))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        solve(a, b)