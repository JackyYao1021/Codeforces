MOD = 998244353

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 1:
        print(0)
        return
    
    sum_arr = 0
    for a in arr:
        sum_arr ^= a
    if sum_arr == 0:
        print(1)
        return 
        
    ans = 0
    highest_bit = 1 << (sum_arr.bit_length() - 1)
    for a in arr:
        if (a & highest_bit) != 0:
            ans += 1
    print(ans % MOD)


    
    
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()