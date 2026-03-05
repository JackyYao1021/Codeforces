def solve(a):
    if a[0] or a[-1]:
        return "Alice"
    else:
        return "Bob"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))