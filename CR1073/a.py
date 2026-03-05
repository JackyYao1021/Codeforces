def solve(n, arr):
    pre = arr[0] % 2
    for i, a in enumerate(arr):
        if (i + a) % 2 != pre:
            return "NO"
    return "YES"
    
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(n, arr))