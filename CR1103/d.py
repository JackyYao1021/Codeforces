from collections import Counter
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    keys = sorted(counter.keys())
    surfix = [0] * len(keys)
    for i in range(len(keys)-1, -1, -1):
        surfix[i] = counter[keys[i]]
        if i != len(keys)-1 and keys[i] + k >= keys[i+1]:
            surfix[i] += surfix[i+1]
        if (surfix[i] - 1) % 2 == 1:
            print("YES")
            return
        if i != 0 and keys[i] - k <= keys[i-1] and (surfix[i-1] - 1) % 2 == 1:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()