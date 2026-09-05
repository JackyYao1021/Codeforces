from collections import Counter
def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    
    counts = [0] * (m+1)
    remains = n
    
    for i in range(1, m+1):
        if i in counter:
            counts[i] = counter[i]
            remains -= counter[i]
        counts[i] += remains 
        counts[i] += counter[2*i] if 2*i in counter else 0
    print(max(counts))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()