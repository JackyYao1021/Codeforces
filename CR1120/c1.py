MOD = 10**9 + 7
def solve():
    n = int(input())    
    arr = list(map(int, input().split()))
    
    ans = []
    diff = [0] * (n + 1)
    
    blocks = [0] * (n + 1)
    for i, mex in enumerate(arr, 1):
        if i * mex < n:
            diff[i * mex] += 1
            if i * (mex + 1) <= n:
                diff[i * (mex+1)] -= 1
            else:
                diff[n] -= 1
        
        for j in range(mex):
            if i * j < n:
                blocks[i * j] += 1
                if i * (j + 1) <= n:
                    blocks[i * (j + 1)] -= 1
                else:
                    blocks[n] -= 1
    
    tmp_diff = 0
    tmp_block = 0

    diff_sum = [0] * (n + 1)
    block_sum = [0] * (n + 1)
    for i in range(n):
        tmp_diff += diff[i]
        tmp_block += blocks[i]
        diff_sum[i] = tmp_diff
        block_sum[i] = tmp_block
    
    if all(x == 0 for x in diff_sum):
        print(0)
        print()
        return
    
    ans = 1
    cur_cnt = 0
    prev = -1
    for i in range(n):
        if diff_sum[i] == 0:
            if block_sum[i] != prev:
                ans = (ans * (cur_cnt + 1)) % MOD
                cur_cnt = 0
                prev = block_sum[i]
    print(ans)
                
                
    

    
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()