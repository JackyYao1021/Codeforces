def solve(n, k, tree):
    # Your implementation here
    return


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print(solve(n, k, arr))