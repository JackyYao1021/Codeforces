def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def digit_sum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

def solve(n):
    while True:
        if gcd(n, digit_sum(n)) > 1:
            print(n)
            break
        n += 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)