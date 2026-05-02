def solve(n, arr):
    div_by_6 = []
    div_by_2 = []
    div_by_3 = []
    rest = []
    for a in arr:
        if a % 6 == 0:
            div_by_6.append(a)
        elif a % 2 == 0:
            div_by_2.append(a)
        elif a % 3 == 0:
            div_by_3.append(a)
        else:
            rest.append(a)
            
    ans = div_by_6 + div_by_2 +  rest + div_by_3 
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)