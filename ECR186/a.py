def solve(n, s):
    cnt_2025 = 0
    cnt_3_same = 0
    cnt_2_same = 0
    cnt_1_same = 0
    for i in range(n-3):
        if s[i] == '2' and s[i+1] == '0' and s[i+2] == '2' and s[i+3] == '6':
            return 0
        elif s[i] == '2' and s[i+1] == '0' and s[i+2] == '2' and s[i+3] == '5':
            cnt_2025 += 1
        elif s[i] == '2' and s[i+1] == '0' and s[i+2] == '2' or s[i+1] == '0' and s[i+2] == '2' and s[i+3] == '6' or s[i] == '2' and s[i+2] == '2' and s[i+2] == '6' or s[i] == '2' and s[i+1] == '0' and s[i+3] == '6':
            cnt_3_same += 1
        elif s[i] == '2' and s[i+1] == '0' or s[i+1] == '0' and s[i+2] == '2' or s[i+2] == '2' and s[i+3] == '6' or s[i] == '2' and s[i+2] == '2' or s[i] == '2' and s[i+3] == '6' or s[i+1] == '0' and s[i+3] == '6':
            cnt_2_same += 1
        elif s[i] == '2' or s[i+1] == '0' or s[i+2] == '2' or s[i+3] == '6':
            cnt_1_same += 1
        
    if cnt_2025 == 0:
        return 0
    elif cnt_2025 > 0 or cnt_3_same > 0:
        return 1
    elif cnt_2_same > 0:
        return 2
    elif cnt_1_same > 0:
        return 3
    else:
        return 4

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        print(solve(n, s))