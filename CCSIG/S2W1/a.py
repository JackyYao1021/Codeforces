from bisect import bisect_right

def solve(x, k):
    forbidden = set()
    for i in range(k, x+1, k):
        forbidden.add(i)
    
    all_numbers = set(range(1, x + 1))
    can_move = all_numbers - forbidden
    list_can_move = sorted(list(can_move))
    
    ans = []
    while x > 0:
        idx = bisect_right(list_can_move, x)
        remove = list_can_move[idx - 1]
        ans.append(remove)
        x -= remove

    print(len(ans))
    print(*ans)    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, k = map(int, input().split())
        solve(x, k)