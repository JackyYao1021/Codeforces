def solve(n, m, grid):
    ans = []
    col_sums = [0] * m
    for i in range(n):
        for j in range(m):
            col_sums[j] += grid[i][j]
    total_sum = sum(col_sums)
    half_sum = total_sum // 2
    finished = False
    for j in range(m):
        if half_sum == 0:
            ans.append("D" * n)
            ans.append("R" * (m - j))
            break
        elif col_sums[j] < half_sum:
            ans.append("R")
            half_sum -= col_sums[j]
        elif col_sums[j] == half_sum:
            ans.append("R")
            ans.append("D" * (n))
            ans.append("R" * (m - j - 1))
            break
        else:
            target = half_sum
            tmp_sum = 0
            for i in range(n-1, -1, -1):
                tmp_sum += grid[i][j]
                if tmp_sum == target:
                    
                    ans.append("D" * i)
                    ans.append("R")
                    
                    ans.append("D" * (n - i))
                    ans.append("R" * (m - j - 1))
                    finished = True
                    break
            
        if finished:
            break
    print((total_sum//2) * (total_sum - total_sum//2) )
    print("".join(ans))
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]
        solve(n, m, grid)
        