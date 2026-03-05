def solve(n, a):
    if a[0] != 1:
        print("NO")
        return
    print("YES")
    return 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        solve(n, a)
    