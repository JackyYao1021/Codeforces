MOD = 676767677

def solve(n, arr):
    ans = 0
    flag = False
    for a in arr:
        if a == 1:
            flag = True
        else:
            ans = (ans + a) % MOD
            flag = False
    if flag:
        ans = (ans + 1) % MOD
    print(ans)
             


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)