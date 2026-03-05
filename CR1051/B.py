def solve():
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    vouchers = list(map(int, input().split()))
    vouchers.sort()
    prices.sort(reverse=True)
    total = 0
    price_idx = 0
    for v in vouchers:
        if price_idx >= n:
            break
        total += sum(prices[price_idx:price_idx+v-1])
        price_idx += v

    if price_idx < n:
        total += sum(prices[price_idx:])
    return total

t = int(input())
for _ in range(t):
    print(solve())