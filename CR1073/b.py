from collections import Counter
def solve(n, arr):
    counter = Counter(arr)
    if not (0 in counter):
        return "NO"
    
    if counter[0] == 1:
        return "YES"
    
    if 1 in counter:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(n, arr))