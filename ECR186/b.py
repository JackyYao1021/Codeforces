def solve(a, b):
    if a < b:
        a, b = b, a

    a1, b1, a2, b2 = a, b, a, b
    layer = 0
    while (a1 >= 0 and b1 >= 0) or (a2 >= 0 and b2 >= 0):
        if layer % 2 == 0:
            a1 -= 2**layer
            b2 -= 2**layer
        else:
            b1 -= 2**layer
            a2 -= 2**layer
        layer += 1
    return layer - 1
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(solve(a, b))