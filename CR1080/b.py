from random import randint
 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


def find_odd(a):
    while a % 2 == 0:
        a //= 2
    return a

def solve(n, arr):
    for i, a in enumerate(arr, 1):
        if find_odd(a) != find_odd(i):
            print("NO")
            return
    print("YES")
    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)