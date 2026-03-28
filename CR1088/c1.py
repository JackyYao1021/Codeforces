def solve(n, k, arr, brr):
    
    left_board = n - k
    right_board = k - 1

    pos = [0] * (n + 1)
    for i, x in enumerate(arr):
        pos[x] = i

    seen = [False] * (n + 1)

    for i in range(n):
        if brr[i] == -1:
            continue

        if i < left_board or i > right_board:
            if brr[i] != arr[i]:
                print("NO")
                return
        else:
            if not (left_board <= pos[brr[i]] <= right_board):
                print("NO")
                return
            if seen[brr[i]]:
                print("NO")
                return
            seen[brr[i]] = True
    print("YES")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        solve(n, k, arr, brr)