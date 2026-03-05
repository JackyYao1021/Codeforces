from collections import defaultdict

def solve(n, arr):
    lm = 0
    rm = len(arr) - 1
    while arr[lm] != 1:
        lm = (lm + 1) % n
    while arr[rm] != 1:
        rm = (rm - 1 + n) % n

    min_dis_from_left = [n] * n
    min_dis_from_right = [n] * n    
    min_dis = [n] * n
    cnt = 0
    for i in range(n):
        if arr[(lm+i)%n] == 1:
            cnt = 0
            min_dis[(lm+i)%n] = 0
            min_dis_from_left[(lm+i)%n] = 0
        else:
            cnt += 1
            min_dis[(lm+i)%n] = min(min_dis[(lm+i)%n], cnt)
            min_dis_from_left[(lm+i)%n] = cnt
    
    for i in range(n):
        if arr[(rm - i + n)%n] == 1:
            cnt = 0
            min_dis[(rm - i + n)%n] = 0
            min_dis_from_right[(rm - i + n)%n] = 0
        else:
            cnt += 1
            min_dis[(rm - i + n)%n] = min(min_dis[(rm - i + n)%n], cnt)
            min_dis_from_right[(rm - i + n)%n] = cnt
            
    
    move_left = 0
    move_right = 0
    
    # state = (move_left, move_right)
    dp = defaultdict(list)
    
    dp[lm] = [(min_dis_from_right[lm], 0) , (0, min_dis_from_left[lm])]
    
    for i in range(1, n):
        idx = (lm + i) % n
        if arr[idx] == 1:
            dp[idx] = dp[(idx-1+n)%n][:]
        else:
            pre_l, pre_r = dp[(idx-1+n)%n]
            if pre_l[0] < min_dis_from_left[idx]:
                dp[idx].append((min_dis_from_right[idx], pre_l[1]))
            else:
                dp[idx].append(pre_l)
            
            if pre_r[1] < min_dis_from_right[idx]:
                dp[idx].append((pre_r[0], min_dis_from_left[idx]))
            else:
                dp[idx].append(pre_r)
                
    lr = dp[(lm-1+n)%n][:]
    
    return min(lr[0][0] + lr[0][1], lr[1][0] + lr[1][1])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip()))
        print(solve(n, arr))