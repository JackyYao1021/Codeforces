from collections import Counter
def solve(n, numbers):
    counter = Counter(numbers)
    limit = n*n - n
    for num, count in counter.items():
        if count > limit:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        numbers = [] 
        for _ in range(n):
            row = list(map(int, input().split()))
            numbers.extend(row)
        solve(n, numbers)