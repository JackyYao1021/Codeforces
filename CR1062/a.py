def solve(a, b, c, d):
    if a == b and b == c and c == d:
        return "Yes"
    return "No"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        print(solve(a, b, c, d))