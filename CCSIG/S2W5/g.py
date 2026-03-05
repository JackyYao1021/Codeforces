from collections import Counter
def divisors(n):
    divs = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            divs.append(i)
            n //= i
    if n > 1:
        divs.append(n)
    return divs

def solve(a):
    divs = divisors(a)
    counter = Counter(divs)
    mx = 0
    root = -1
    for key, value in counter.items():
        if value > mx:
            mx = value
            root = key
    
    print(mx)
    ans = []
    tmp = 1
    for i in divs:
        if i != root:
            tmp *= i

    for i in range(mx):
        ans.append(root)
        
    ans[-1] *= tmp
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        solve(a)