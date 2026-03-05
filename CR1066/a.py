from collections import Counter
def solve(arr):
    counter = Counter(arr)
    ans = 0
    for key, value in counter.items():
        if key > value:
            ans += value
        elif key < value:
            ans += value - key
    return ans  

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))