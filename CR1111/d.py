def solve():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    order = sorted(range(n), key=lambda x: arr[x])
    mask = 0
    
    for target, original in enumerate(order):
        mask |= original ^ target
        
    if mask == 0:
        print(0)
    else:
        print(1 << (mask.bit_length() - 1))

if __name__ == "__main__":
     t = int(input())
     for _ in range(t):
         solve()