t = int(input())

for _ in range(t):
    n = int(input())
    hills = list(map(int, input().split()))
    
    L_set = set()
    R_set = set()
    cur_h = 0 
    for i in range(n):
        if hills[i] > cur_h:
            L_set.add(i)
            cur_h = hills[i]
    cur_h = 0
    for i in range(n-1, -1, -1):
        if hills[i] > cur_h:
            R_set.add(i)
            cur_h = hills[i]
    
    left = 0
    right = n - 1
    left_idx = set()
    deque = []
    
    for e in L_set:
        deque.append(e)
        

    while left < n-1:
        if 
        