t = int(input())
for _ in range(t):
    score = 0
    FJ_side = 0
    FJ_time = 0
    n, m = map(int, input().split())
    for _ in range(n):
        time, side = map(int, input().split())
        
        if (time - FJ_time) % 2 == abs(side - FJ_side):
            score += (time - FJ_time)
        else:
            score += (time - FJ_time) - 1
        FJ_side = side
        FJ_time = time
    score += (m - FJ_time)
    print(score)