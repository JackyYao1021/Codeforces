def solve(n, arr):
    odd_cnt = 0
    even_cnt = 0
    
    for a in arr:
        if a % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    
    if odd_cnt == 0:
        print("NO")
    elif even_cnt == 0 and odd_cnt % 2 == 0:
        print("NO")
    else:
        print("YES")
        


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)    