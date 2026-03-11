def solve(n, arr):
    if arr[0] == 1:
        print("Bob")
        return
    rest = sum(arr) - n
    if sum(arr) - n == arr[0] - 1:
        print("Alice")
        return
    if rest % 2 == 0:
        print("Alice")
    else:
        print("Bob")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)