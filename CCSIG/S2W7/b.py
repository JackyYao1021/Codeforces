def solve(a):
    while a & 1 == 0:
        a >>= 1
    
    if a == 1:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        solve(a)
        