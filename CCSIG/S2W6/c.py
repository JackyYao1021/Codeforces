from collections import Counter

def solve(n, k, s):
    counter = Counter(s)
    odds = []
    for c in counter:   
        if counter[c] % 2 == 1:
            odds.append(c)
    
    if len(odds) > k+1:
        print("NO")
        return
    print("YES")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        solve(n, k, s)