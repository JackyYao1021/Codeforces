def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    count_1 = arr.count(1)
    count_0 = arr.count(0)
    if count_0 > count_1:
        print("Elsie")
    else:
        print("Bessie")
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()