def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    a = arr[0]
    b = arr[-1]
    print(gcd(a, b))
    return 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()