from collections import Counter
def solve(n, b):
    zeros = b.count(0)
    return min(sum(b) - (n - 1), n - zeros)
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        print(solve(n , b))