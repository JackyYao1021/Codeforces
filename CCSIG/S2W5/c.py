def divisors(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return divs


def solve(n, x, y):
    diff = y - x
    divs = divisors(diff)
    divs.sort()
    mx = float('inf')
    ans = []
    n -= 1
    for d in divs:
        tmp = n - diff // d
        if tmp < 0:
            continue
        
        for a in range(x, y + 1, d):
            ans.append(a)
        idx = x
        while tmp > 0:
            idx -= d
            if idx <= 0:
                break
            ans.append(idx)
            tmp -= 1
        
        idx = y
        while tmp > 0:
            idx += d
            ans.append(idx)
            tmp -= 1
        
        print(*ans)
        return
            
        
        
        




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x, y = map(int, input().split())
        solve(n, x, y)