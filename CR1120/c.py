def solve():
    n = int(input())    
    arr = list(map(int, input().split()))
    
    ans = []
    diff = [0] * (n + 1)
    for i, mex in enumerate(arr, 1):
        if i * mex < n:
            diff[i * mex] += 1
            if i * (mex + 1) <= n:
                diff[i * (mex+1)] -= 1
            else:
                diff[n] -= 1
    
    tmp = 0
    for i in range(n):
        tmp += diff[i]
        if tmp == 0:
            ans.append(i)

    print(len(ans))
    print(*ans)
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()