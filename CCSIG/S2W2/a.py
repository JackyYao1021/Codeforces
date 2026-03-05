def solve(n, arr):
    ans = 10**5+1
    for a in arr:
        ans = min(ans, abs(a))
    print(ans)



if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    solve(n, arr)