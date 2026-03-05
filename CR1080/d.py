from random import randint
 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM



def solve(n, arr):
    ans = [0] * n
    total = (arr[0] + arr[-1]) // (n-1)
    tmp = 0 
    for i in range(n-1):
        sub_total = arr[i] - arr[i+1] 
        arr[i] = (total - sub_total - 2*tmp) // 2
        tmp += arr[i]
    arr[-1] = total - tmp
    print(" ".join(map(str, arr))) 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)