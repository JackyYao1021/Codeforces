from collections import Counter
def solve(n, arr):
    count = Counter(arr)
    min_value = min(count.keys())
    max_value = max(count.keys())
    keys = list(count.keys())
    if len(keys) == 1:
        return "YES"
    for key, value in count.items():
        if key != min_value and key != max_value and value % 2 != 0:
            return "NO"
        elif key == min_value and value % 2 == 0:
            return "NO"
    return "YES"
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(n, arr))