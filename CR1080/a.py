from random import randint
 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


def solve(n, a):
    if 67 in a:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        solve(n, a)