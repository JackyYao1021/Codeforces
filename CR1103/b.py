def solve():
    n, k = map(int, input().split())
    arr = input()
    for i in range(k):
        tmp = 0
        for j in range(i, n, k):
            tmp += int(arr[j])
        if tmp % 2 != 0:
            print("NO")
            return
    print("YES")
            




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()