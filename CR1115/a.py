from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    sorted_counts = sorted(counter.values(), reverse=True)
         




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()