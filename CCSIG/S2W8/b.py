from collections import Counter
def solve(n, arr):
    counter = Counter(arr)
    if len(counter.keys()) == 1:
        print("Yes")
        return
    elif len(counter.keys()) == 2:
        keys = list(counter.keys())
        if abs(counter[keys[0]] - counter[keys[1]]) == 1 or counter[keys[1]] - counter[keys[0]] == 0:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)