from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    counter = Counter(arr)
    keys = sorted(counter.keys())
    cur = 0 
    if counter[0] == 1:
        print("NO")
        return
    
    for key in keys:
        if cur == key:
            if counter[key] >= 3:
                cur += 1
            else:
                # when not enough
                break
        else:
            break
    print("YES")
    set_a = set()
    set_b = set()
    ans = ["C"] * n
    for i, c in enumerate(arr):
        if c < cur:
            if c not in set_a:
                set_a.add(c)
                ans[i] = "A"
            elif c not in set_b:
                set_b.add(c)
                ans[i] = "B"
        elif c == cur:
            if c not in set_a:
                set_a.add(c)
                ans[i] = "A"
            elif c not in set_b:
                set_b.add(c)
                ans[i] = "B"
        else:
            ans[i] = "C"
    print("".join(ans))
            
    





if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()