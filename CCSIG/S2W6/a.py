def solve(n, k, a):
    if k == 1:
        prev = a[0]
        for i in range(1, n):
            if a[i] < prev:
                print("NO")
                return
            prev = a[i]
        print("YES")
        return
    print("YES")
    return 



if __name__ == "__main__":
    
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        solve(n, k, a)