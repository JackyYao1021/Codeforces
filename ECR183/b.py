
def solve(n, k, actions):
    c0 = actions.count('0')
    c1 = actions.count('1')
    cq = k - c0 - c1
    
    plus_start = c0 + cq + 1
    plus_end = n - c1 - cq
    
    possible_starts = c0 + 1
    possible_ends = n - c1
    
    ans = []
    
    for i in range(1, n + 1):
        if plus_start <= i <= plus_end:
            ans.append('+')
        elif possible_starts <= i <= possible_ends:
            if possible_ends - possible_starts + 1 > cq:
                ans.append('?')
            else:
                ans.append('-')
        else:
            ans.append('-')
    return ''.join(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        actions = str(input())
        print(solve(n, k, actions))