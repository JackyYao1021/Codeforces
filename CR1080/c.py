from random import randint
from collections import Counter 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM



def solve(n, arr):
    dp = [float('inf')] * 7
    for i in range(1, 7):
        if arr[0] != i:
            dp[i] = 1
        else:
            dp[i] = 0
        
    
    for i in range(1, n):
        a = arr[i]
        tmp_dp = [float('inf')] * 7
        for u in range(1, 7):
            if u == a:
                tmp = 0
            else:
                tmp = 1
            opposite = (7 - u)
            best = float('inf')
            for v in range(1, 7):
                if u != v and v != opposite:
                    best = min(best, dp[v])
            tmp_dp[u] = best + tmp
        dp = tmp_dp
    
    print(min(dp[1:]))
    
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)