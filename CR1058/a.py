from collections import Counter
def solve(arr):
    count = Counter(arr)
    keys = list(count.keys())
    sorted_keys = sorted(keys)
    for i in range(0, len(sorted_keys)):
        if sorted_keys[i] != i:
            return i
    return len(sorted_keys)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))