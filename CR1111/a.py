def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    one_count = arr.count(1)
    neg_count = arr.count(-1)
    
    if abs(one_count - neg_count) % 4 == 0:
        print("YES")
        return 
    print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()