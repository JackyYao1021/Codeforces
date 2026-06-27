from collections import defaultdict
MOD = 10**9+7

def factorise(arr):
    dic = defaultdict(int)
    for num in arr:
        for i in range(2, int(num**0.5) + 1):
            while num % i == 0:
                dic[i] += 1
                num //= i
        if num > 1:
            dic[num] += 1
    return dic

def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    dic = factorise(arr)
    ans = 1
    for value in dic.values():
        ans = ans * (value + 1) % MOD
    print(ans) 
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()