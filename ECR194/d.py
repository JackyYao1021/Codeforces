def solve():
    n = int(input())
    s = input().strip()
    
    if s[0] == '0' or '00' in s:
        print(-1)
        return
    
    stack = [('0', 1)]
    prev = s[0]
    tmp = 1
    for i in range(1, n):
        if s[i] == prev:
            tmp += 1
        else:
            stack.append((prev, tmp))
            prev = s[i]
            tmp = 1
    
    stack.append((s[-1], tmp))
    
    if len(stack) < 3:
        print(1)
        return
    
    ans = 0
    for i in range(1, len(stack) - 1):
        left_sign = stack[i - 1][0]
        right_sign = stack[i + 1][0]
        cur_sign, cur_count = stack[i]
        
        if cur_sign == '0':
            continue
        if left_sign == '0' and right_sign == '0':
            if cur_count % 2 == 0:
                ans = max(ans, 2)
            else:
                ans = max(ans, 1)
        elif left_sign == '0' or right_sign == '0':
            ans = max(ans, 2)
        elif cur_count == 2:
            ans = max(ans, 3)
        else:
            ans = max(ans, 2)
    print(ans)
            
        



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()