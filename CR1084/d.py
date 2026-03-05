def solve(n, x, y, arr):
    mid = arr[x:y]
    rest = arr[:x] + arr[y:]
    idx_min_mid = mid.index(min(mid))
    new_mid = mid[idx_min_mid:] + mid[:idx_min_mid]
    if len(rest) == 0:
        print(*new_mid)
        return
    else:
        for i in range(len(rest)):
            if rest[i] > new_mid[0]:
                print(*rest[:i], *new_mid, *rest[i:])        
                return
        print(*rest, *new_mid)
        
        
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x, y = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, x, y, arr)