from collections import Counter
from random import randint
 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM
    
def solve(n, arr, brr):
    prefix_sum = []
    for i in range(n):
        if i == 0:
            prefix_sum.append(brr[i])
        else:
            prefix_sum.append(prefix_sum[i-1] + brr[i])
    
    arr = [Wrapper(a) for a in arr]
    counter = Counter(arr)
    keys = sorted(counter.keys())
    
    total = n
    idx = n-1
    ans = [0]
    for difficulty in keys:
        while idx >= 0 and prefix_sum[idx] > total:
            idx -= 1
        if idx >= 0:
            ans.append((idx+1) * difficulty)
            count = counter[difficulty]
            total -= count
        else:
            break
    print(max(ans))


# def solve_new(n, arr, brr):
#     for i in range(1, n):
#         brr[i] += brr[i - 1]

#     counter = Counter(arr)
#     items = sorted(counter.items())

#     total = n
#     idx = n - 1
#     best = 0
#     ps = brr

#     for difficulty, count in items:
#         while idx >= 0 and ps[idx] > total:
#             idx -= 1
#         if idx < 0:
#             break
#         val = (idx + 1) * difficulty
#         if val > best:
#             best = val
#         total -= count

#     print(best)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        solve(n, arr, brr) 