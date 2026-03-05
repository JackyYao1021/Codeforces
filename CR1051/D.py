from itertools import combinations

MOD = 10**9 + 7

def is_good(subseq):
    k = len(subseq)
    for i in range(k):
        for j in range(i+1, k):
            for l in range(j+1, k):
                if subseq[i] > subseq[j] > subseq[l]:
                    return False
    return True

def solve(arr):
    n = len(arr)
    count = 0
    for mask in range(1<<n):
        subseq = [arr[i] for i in range(n) if (mask>>i)&1]
        if is_good(subseq):
            count = (count + 1) % MOD
    return count

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))