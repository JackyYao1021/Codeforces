def solve(l, a, b):
    visited = set()
    visited.add(a)
    x = (a + b) % l
    while x not in visited:
        visited.add(x)
        x = (x + b) % l
    return max(visited)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        l, a, b = map(int, input().split())
        print(solve(l, a, b))
    