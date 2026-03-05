def solve(n, arr, costs):
    dp = [[0] * n for _ in range(2)]
    
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        costs = list(map(int, input().split()))
        print(solve(n, arr, costs))