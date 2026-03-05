from collections import Counter
def solve(arr):
    count = Counter(arr)
    diff_count = len(count)
    return 2*diff_count - 1
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))