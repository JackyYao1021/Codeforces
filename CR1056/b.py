def solve(n, k):
    if k == n * n - 1:
        print("NO")
        return

    print("YES")
    grid = [['' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(0, n - 1, 2):
            grid[i][j] = 'R'
            grid[i][j+1] = 'L'


    if n % 2 == 1:
        for i in range(0, n - 1, 2):
            grid[i][n-1] = 'D'
            grid[i+1][n-1] = 'U'

    if n % 2 == 1:
        grid[n-1][n-1] = 'L'

    escapes_to_create = k


    if escapes_to_create % 2 == 1:
        if n % 2 == 1:

            grid[n-1][n-1] = 'D'
        else:
            grid[0][0] = 'U'
            grid[0][1] = 'D'
        escapes_to_create -= 1


    pairs_to_break = escapes_to_create // 2

    for i in range(n):
        if pairs_to_break == 0:
            break
        for j in range(0, n - 1, 2):
            if pairs_to_break == 0:
                break
            if n % 2 == 0 and i == 0 and j == 0 and k % 2 == 1:
                continue
            
            grid[i][j] = 'U'
            grid[i][j+1] = 'U'
            pairs_to_break -= 1

    if pairs_to_break > 0 and n % 2 == 1:
        for i in range(0, n - 1, 2):
            if pairs_to_break == 0:
                break
            grid[i][n-1] = 'L'
            grid[i+1][n-1] = 'L'
            pairs_to_break -= 1

    for i in range(n):
        print("".join(grid[i]))
        


def init_maze(n):
    grid = [["."]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i+j) <= n-1 and j < i:
                grid[i][j] = "U"
            elif (i+j) < n-1 and j >= i:
                grid[i][j] = "R"
            elif (i+j) > n-1 and j <= i:
                grid[i][j] = "L"
            else:
                grid[i][j] = "D"
    return grid

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        solve(n, k)