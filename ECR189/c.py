def solve(n, A, B):
    idx = 0
    ans = 0
    while idx < n:
        if A[idx] == B[idx]:
            idx += 1
            continue
        else:
            if idx == n-1:
                ans += 1
                break
            else:
                if A[idx] == A[idx+1] and B[idx] == B[idx+1]:
                    idx += 2  
                elif A[idx] != A[idx+1] and B[idx] != B[idx+1]:
                    ans += 1
                    idx += 1
                else:
                    ans += 1
                    idx += 2
            
    print(ans)
        


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = input().strip()
        B = input().strip()
        solve(n, A, B)