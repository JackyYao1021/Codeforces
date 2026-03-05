from random import randint
 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM
    
def solve(n, ax, ay, bx, by, xs, ys):
    dic = {}
    xs = [Wrapper(x) for x in xs]
    for i in range(n):
        if xs[i] not in dic:
            dic[xs[i]] = (ys[i], ys[i])
        else:
            if ys[i] < dic[xs[i]][0]:
                dic[xs[i]] = (ys[i], dic[xs[i]][1])
            if ys[i] > dic[xs[i]][1]:
                dic[xs[i]] = (dic[xs[i]][0], ys[i])
    
    length = len(dic.keys())
    edge_points = []
    for key in sorted(dic.keys()):
        edge_points.append(dic[key])
    
    
    dp = [0, 0]
    diff = abs(edge_points[0][0]-edge_points[0][1])
    dp[0] = abs(ay-edge_points[0][0]) + diff #  bottom - top
    dp[1] = abs(ay-edge_points[0][1]) + diff # top - bottom
    
    for i in range(1, length):
        diff = abs(edge_points[i][0]-edge_points[i][1])
        dp[0], dp[1] = min(dp[0] + abs(edge_points[i-1][1]-edge_points[i][0]) + diff, dp[1] + abs(edge_points[i-1][0]-edge_points[i][0]) + diff), min(dp[0] + abs(edge_points[i-1][1]-edge_points[i][1]) + diff, dp[1] + abs(edge_points[i-1][0]-edge_points[i][1]) + diff)
    
    ans = min(dp[0] + abs(edge_points[length-1][1]-by),
              dp[1] + abs(edge_points[length-1][0]-by))
    print(ans+bx-ax)


if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n, ax, ay, bx, by = map(int, input().split())
        xs = list(map(int, input().split()))
        ys = list(map(int, input().split()))
        solve(n, ax, ay, bx, by, xs, ys)
        
        