def solve():
    n, m = map(int, input().split())
    
    relation_matrix = [[0] * n for _ in range(n)]
    ans = [0] * n
    for _ in range(m):
        o, i, j = map(int, input().split())
        relation_matrix[i-1][j-1] = o 
        relation_matrix[j-1][i-1] = o
         
    relation_1_cnt = [0] * n
    relation_2_cnt = [0] * n
    for i in range(n):
        for j in range(n):
            if relation_matrix[i][j] == 1:
                relation_1_cnt[i] += 1
            elif relation_matrix[i][j] == 2:
                relation_2_cnt[i] += 1
    
    
    selected = [False] * n
    selected_count = 0
    select_list = []
    select = False
    
    for k in range(n):
        select = False
        for i in range(n):
            if selected[i]:
                continue
            if relation_1_cnt[i] == 0:
                selected[i] = True
                selected_count += 1
                select_list.append([i, k-n])
                select = True
                for j in range(n):
                    if relation_matrix[i][j] == 1 and not selected[j]:
                        relation_1_cnt[j] -= 1
                    elif relation_matrix[i][j] == 2 and not selected[j]:
                        relation_2_cnt[j] -= 1
                break
            elif relation_2_cnt[i] == 0:
                selected[i] = True
                selected_count += 1
                select_list.append([i, n-k])
                select = True
                for j in range(n):
                    if relation_matrix[i][j] == 1 and not selected[j]:
                        relation_1_cnt[j] -= 1
                    elif relation_matrix[i][j] == 2 and not selected[j]:
                        relation_2_cnt[j] -= 1
                break
        if not select:
            print("NO")
            return
    for i in range(n):
        ans[select_list[i][0]] = select_list[i][1]
    print("YES")
    print(" ".join(map(str, ans)))
        
        
               
            
            
        
        
        
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()