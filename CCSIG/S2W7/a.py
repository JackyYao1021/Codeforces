def solve(w, h, n):
    cnt_w = 1
    while w % 2 == 0:
        w //= 2
        cnt_w *= 2
        
    cnt_h = 1
    while h % 2 == 0:
        h //= 2
        cnt_h *= 2
    ans = cnt_w * cnt_h
    if ans >= n:
        print("YES")
    else:
        print("NO")
    # print(ans)
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        w, h, n = map(int, input().split())
        solve(w, h, n)