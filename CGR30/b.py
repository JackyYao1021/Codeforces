def solve(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if (arr[i] % arr[j]) % 2 == 0:
                return f"{arr[j]} {arr[i]}"
    return "-1"
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))