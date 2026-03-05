def solve(n):
    
    if n % 2 == 0:
        return (n - 4)// 2 + 1
    else:
        return (n - 3)// 2 + 1
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))
    
    