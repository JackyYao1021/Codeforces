# 0 -> 0 0
# 0 -> 1 2
# 1 -> 1 0
# 1 -> 1 3
# 2 -> 2 3
# 2 -> 2 0
# 3 -> 3 3
# 3 -> 2 1

def cal(a, b, c, d):
    mx, mn = max(a, d), min(a, d)
    return max(4*b, 4 * ((mx + b + 1) // 2), 4 * ((mx + b + mn + 2) // 3)) - a - b - c - d
    
def solve():
    n, q = map(int, input().split())
    s = input().strip()
    prefix = [[0] * 4]
    for i in range(1, n):
        prefix.append(prefix[i-1][:])
        if s[i-1:i+1] == "00":
            prefix[i][0] += 1
        elif s[i-1:i+1] == "01":
            prefix[i][1] += 1
        elif s[i-1:i+1] == "10":
            prefix[i][2] += 1
        elif s[i-1:i+1] == "11":
            prefix[i][3] += 1
    
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        if s[r] == '0' and s[l] == '0':
            print(cal(prefix[r][0] - prefix[l][0]+1, prefix[r][1] - prefix[l][1], prefix[r][2] - prefix[l][2], prefix[r][3] - prefix[l][3]))
        elif s[r] == '0' and s[l] == '1':
            print(cal(prefix[r][0] - prefix[l][0], prefix[r][1] - prefix[l][1]+1, prefix[r][2] - prefix[l][2], prefix[r][3] - prefix[l][3]))
        elif s[r] == '1' and s[l] == '0':
            print(cal(prefix[r][0] - prefix[l][0], prefix[r][1] - prefix[l][1], prefix[r][2] - prefix[l][2]+1, prefix[r][3] - prefix[l][3]))
        elif s[r] == '1' and s[l] == '1':
            print(cal(prefix[r][0] - prefix[l][0], prefix[r][1] - prefix[l][1], prefix[r][2] - prefix[l][2], prefix[r][3] - prefix[l][3]+1))




if __name__ == "__main__":
    solve()