def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    s = input().strip()
    
    left_one_idx = 0
    right_zero_idx = n - 1
    
    one_left = [-1] * n
    zero_right = [-1] * n
    one_cnt = 0
    for i in range(n):
        if arr[i] == 1:
            one_cnt += 1
        else:
            one_left[i] = one_cnt
    zero_cnt = 0
    tmp = 0
    for i in range(n - 1, -1, -1):
        if arr[i] == 0:
            zero_cnt += 1
        else:
            zero_right[i] = zero_cnt
            tmp += zero_cnt
    ans = [tmp] * (n+1)      

    cnt_1 = 0
    cnt_0 = 0
    
    for i, c in enumerate(s):
        if tmp == 0:
            ans[i+1] = 0
            continue
        if c == "1":
            #find next 1
            while left_one_idx < n and arr[left_one_idx] != 1:
                left_one_idx += 1
            if left_one_idx == n:
                ans[i+1] = tmp
            else:
                tmp -= (zero_right[left_one_idx] - cnt_0)
                ans[i+1] = tmp
                cnt_1 += 1
                left_one_idx += 1
        else:
            while right_zero_idx >= 0 and arr[right_zero_idx] != 0:
                right_zero_idx -= 1
            if right_zero_idx < 0:
                ans[i+1] = tmp
            else:
                tmp -= (one_left[right_zero_idx] - cnt_1)
                ans[i+1] = tmp
                cnt_0 += 1
                right_zero_idx -= 1
    print(*ans)
            
    
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()