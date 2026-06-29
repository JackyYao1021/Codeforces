from collections import defaultdict

def devisors(n):
    divisors = defaultdict(int)

    i = 2
    while i * i <= n:
        while n % i == 0:
            divisors[i] += 1
            n //= i
        i += 1

    if n > 1:
        divisors[n] += 1

    return divisors


def solve():
    n = int(input())
    divisors_list = devisors(n)
    total = 0
    # print(divisors_list)
    for prime, count in divisors_list.items():
        total += count + 1

    print(total - 1)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()