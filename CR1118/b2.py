from collections import Counter

def solve():
    n, total_m = map(int, input().split())
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    ans = []

    for i in range(1, total_m+1):
        best_cut = 2 ** i
        
        multis = set()
        multis.add(1)
        for a in counter:
            if a % best_cut == 0:
                multis.add(a // best_cut)
        
        mx = 0
        for a in multis:
            tmp = 0
            
            for b, freq in counter.items():
                tmp += min(b // a, best_cut-1) * freq
            tmp += counter[a * best_cut] if a * best_cut in counter else 0
            mx = max(mx, tmp)
            
        ans.append(mx)
    print(*ans)

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()