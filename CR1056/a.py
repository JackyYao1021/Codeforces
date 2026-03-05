from math import log, floor
def solve(n):
    ans = 0
    win_poll = n
    lose_poll = 0
    while win_poll > 1:
        win_tmp = win_poll // 2
        lose_tmp = lose_poll // 2
        ans += win_tmp + lose_tmp


        win_poll = win_poll - win_tmp

        lose_poll = lose_poll - lose_tmp
        lose_poll += win_tmp
    
    while lose_poll > 1:
        lose_tmp = lose_poll // 2
        ans += lose_tmp
        lose_poll = lose_poll - lose_tmp

    return ans+1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))