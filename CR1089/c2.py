def gdc(a,b):
    if b == 0:
        return a
    return gdc(b, a % b)

def lcm(a, b):
    return a // gdc(a, b) * b

def solve(n, arr, brr):
    divisors = []
    for i in range(n-1):
        d = gdc(arr[i], arr[i+1])
        divisors.append(d)
    
    ans = 0
    if arr[0] != divisors[0]:
        ans += 1
    for i in range(1, n-1):
        need = lcm(divisors[i - 1], divisors[i])
        if arr[i] > need:
            ans += 1
            
    if arr[n-1] != divisors[n-2]:
        ans += 1
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        solve(n, arr, brr)