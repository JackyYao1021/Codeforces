
def solve(a, b, c):
    n = len(a)
    def check(x, y):
        cnt = 0
        for d in range(n):
            bad = False
            for i in range(n):
                if x[i] >= y[(i+d) % n]:
                    bad = True
                    break    
            if not bad:
                cnt += 1
        return cnt
                
    ab_cnt  = check(a, b)
    bc_cnt  = check(b, c)
                
    return n * ab_cnt * bc_cnt




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        print(solve(a, b, c))