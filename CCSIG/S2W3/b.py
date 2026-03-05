from collections import Counter 
def solve(n, arr):
    arr.sort(reverse=True)
    brr = []
    crr = []
    mx = arr[0]
    idx = 0
    for a in arr:
        if a == mx:
            crr.append(a)
            idx += 1
        else:
            break
    if idx == n:
        print(-1)
    else:
        brr = arr[idx:]
        print(f"{len(brr)} {len(crr)}")
        print(*brr)
        print(*crr)
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)