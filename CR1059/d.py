def query(type, l, r):
    print(f"{type} {l} {r}", flush=True)
    res = int(input())
    return res

def solve(n):
    window_size = query(2, 1, n) - ((1 + n) * n // 2)
    left = 1
    right = n
    while left < right:
        if right - left + 1 == window_size:
            break
        mid = (left + right) // 2
        original = query(1, left, mid)
        new = query(2, left, mid)
        if new - original == window_size:
            right = mid
        elif new - original == 0:
            left = mid + 1
        else:
            left_part = query(2, left, left+(new-original)-1) - query(1, left, left + new - original - 1)
            if left_part == new - original:
                right = left + new - original - 1
                left = right - window_size + 1
            else:
                left = mid - (new - original) + 1
                right = left + window_size - 1
            break
    print(f"! {left} {right}", flush=True)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)
        