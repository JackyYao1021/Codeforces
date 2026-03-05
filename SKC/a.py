def solve(x, a, b, c):
    credits = x + a + b + c
    if 120 <= credits <= 160:
        return "YES"
    else:
        return "NO"
    
if __name__ == "__main__":
    x, a, b, c = map(int, input().split())
    result = solve(x, a, b, c)
    print(result)