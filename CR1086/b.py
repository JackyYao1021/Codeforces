from heapq import heappush, heappop

def solve(n, k, p, m, cards):
    target = cards[p - 1]

    if k == n:
        print(m // target)
        return

    rest = cards[:p-1] + cards[p:] + [0]
    # print(rest)

    pref = [0] * (n-k+1)
    heap = []

    for i in range(k):
        heappush(heap, rest[i])

    cnt = 1
    
    for i in range(k, n):
        mn = heappop(heap)
        pref[cnt] = pref[cnt - 1] + mn
        heappush(heap, rest[i])
        cnt += 1

    if p <= k:
        first = target
    else:
        first = pref[p - k] + target

    if first > m:
        print(0)
        return

    round_total = pref[n - k] + target
    ans = 1 + ((m - first) // round_total)
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k, p, m = map(int, input().split())
        cards = list(map(int, input().split()))
        solve(n, k, p, m, cards)