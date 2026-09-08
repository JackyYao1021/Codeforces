from math import log2, ceil, floor
def solve():
    x, y = map(int, input().split())
    
    mx = x + y 
    
    x_prime = 0
    
    for i in range(mx.bit_length(), -1, -1):
        if (1 << i) & mx:
            if (x_prime + (1 << i)) <= x:
                x_prime += (1 << i)
    
    print(mx, x - x_prime)
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()