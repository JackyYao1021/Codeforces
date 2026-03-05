def solve(n):
    return (3 - n % 3) % 3
    
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))