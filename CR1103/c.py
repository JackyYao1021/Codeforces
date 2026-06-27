def all_values(a, x):
    values = []
    cnt = 0
    while True:
        values.append(a)
        if a == 0:
            break
        a //= x
    return values



def solve():
    a, b, x = map(int, input().split())

    values_a = all_values(a, x)
    values_b = all_values(b, x)

    ans = float("inf")
    for cnt_a, val_a in enumerate(values_a):
        for cnt_b, val_b in enumerate(values_b):
            ans = min(ans, cnt_a + cnt_b + abs(val_a - val_b))
    print(ans)




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()