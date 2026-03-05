def solve(n):
    if n % 3 == 1 or n % 3 == 2:
        return "First"
    else:
        return "Second"
    return ""
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))