from math import log2, floor
def solve(a, b):
    if a == b:
        print("0")
        return 0 
    c = a ^ b
    if floor(log2(c)) <= floor(log2(a)):
        if c <= a:   
            print("1")
            print(c)
            return 0        
        else:
            print("2")
            x = 1 << floor(log2(a))
            print(f"{c ^ x} {x}")
            return 0
    else:
        print("-1")
        return 0
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        solve(a, b)