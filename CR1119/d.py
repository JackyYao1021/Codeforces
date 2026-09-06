from collections import Counter
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    
    if arr.count(0) == 1: 
        print("NO")
        return
    print("YES")
    setA = False
    ans = ["C"] * n
    for i in range(n):
        if arr[i] == 0 and not setA:
            ans[i] = "A"
            setA = True
        elif arr[i] == 0 and setA:
            ans[i] = "B"
    print("".join(ans))




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()