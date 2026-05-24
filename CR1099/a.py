def solve():
    n = int(input())
    not_used = set([i for i in range(1, 2*n+1)])
    ans = []
    ans.append(not_used.pop())
    for _ in range(n-1):
        next = not_used.pop()
        ans.append(next)
        if ans[-1] + ans[-2] in not_used:
            not_used.remove(ans[-1]+ans[-2])
    
    print(*ans)
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()