def solve(n, q, s, queries):
    ans = 0
    cnt_i_next = 0
    cnt_question_next_XV = 0
    cnt_question_next_I = 0
    cnt_question_next_q = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 10
        elif s[i] == 'V':
            ans += 5
        elif s[i] == 'I':
            if i < n - 1 and s[i + 1] == 'X' or s[i + 1] == 'V':
                ans += -1
            elif i < n - 1 and s[i + 1] == 'I':
                ans += 1    
            elif i < n - 1 and s[i + 1] == "?":
                cnt_i_next += 1
            else:
                ans += 1
        elif s[i] == '?':
            if i < n - 1 and s[i + 1] == 'X' or s[i + 1] == 'V':
                cnt_question_next_XV += 1                
            elif i < n - 1 and s[i + 1] == 'I':
                cnt_question_next_I += 1
            elif i < n - 1 and s[i + 1] == "?":
                cnt_question_next_q += 1
            else:
                cnt_question_next_XV += 1
                
    for cx, cv, ci in queries:
        while ci and cnt_i_next:
            ans += -1
            cnt_i_next -= 1
            ci -= 1
            
                
            
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        s = input().strip()
        queries = []
        for __ in range(q):
            cx, cv, ci = map(int, input().split())
            queries.append((cx, cv, ci))
        print(solve(n, q, s, queries))