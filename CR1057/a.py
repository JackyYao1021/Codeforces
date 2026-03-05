from collections import Counter
def solve(beauty):
    return len(Counter(beauty))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        beauty = list(map(int, input().split()))
        print(solve(beauty))
