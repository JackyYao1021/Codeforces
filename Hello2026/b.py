from collections import Counter
def solve(n, k, a):
    counter = Counter(a)
    cnt = 0
    for i in range(k-1):
        if not i in counter:
            return i
    return k-1
        
        
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(n, k, a))
                 