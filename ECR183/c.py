def solve(s):
    c_a = s.count('a')
    c_b = s.count('b')
    
    if c_a == c_b:
        return 0
    
    diff = c_a - c_b
    n = len(s)
    
    prefix_map = {0: 0}
    balance = 0
    min_len = n + 1
    
    for i, ch in enumerate(s, 1):
        if ch == 'a':
            balance += 1
        elif ch == 'b':
            balance -= 1
        
        target = balance - diff
        if target in prefix_map:
            min_len = min(min_len, i - prefix_map[target])
        
        prefix_map[balance] = i
        
    return min_len if min_len < n else -1
    
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = str(input())
        print(solve(s))