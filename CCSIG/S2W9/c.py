def solve(n, arr):
    Sereja = 0
    Dima = 0
    
    while arr:
        mx = max(arr[0], arr[-1])
        if arr[0] == mx:
            Sereja += arr[0]
            arr.pop(0)
        else:
            Sereja += arr[-1]
            arr.pop()
        if not arr:
            break
        mx = max(arr[0], arr[-1])
        if arr[0] == mx:
            Dima += arr[0]
            arr.pop(0)
        else:
            Dima += arr[-1]
            arr.pop()   
    print(Sereja, Dima)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    solve(n, arr)