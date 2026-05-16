def solve(n, arr):
    if 100 in arr:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)