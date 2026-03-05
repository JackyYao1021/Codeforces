def solve(n, s, x, arr):
    sum_arr = sum(arr)
    if s < sum_arr:
        print("NO")
        return
    else:
        if (s - sum_arr)  % x == 0:
            print("YES")
        else:
            print("NO") 


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, s, x = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, s, x, arr)