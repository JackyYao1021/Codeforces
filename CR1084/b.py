def solve(n, arr):
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            print(1)
            return
    print(n)
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)