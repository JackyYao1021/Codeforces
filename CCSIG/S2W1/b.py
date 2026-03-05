def solve(a, b, x_k, y_k, x_q, y_q):
    directions = [(1,1), (1, -1), (-1,1), (-1,-1)] 
    length = [(a, b), (b, a)]
    kill_kings = set()
    for dx, dy in directions:
        for l_x, l_y in length:
            nx = dx*l_x + x_k
            ny = dy*l_y + y_k
            kill_kings.add((nx, ny))
            
    kill_queens = set()
    for dx, dy in directions:
        for l_x, l_y in length:
            nx = dx*l_x + x_q
            ny = dy*l_y + y_q
            kill_queens.add((nx, ny))
        
    print(len(kill_kings.intersection(kill_queens)))



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        x_k, y_k = map(int, input().split())
        x_q, y_q = map(int, input().split())
        solve(a, b, x_k, y_k, x_q, y_q)