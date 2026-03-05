def solve(R0, X, D, n, s):
    diff = X - R0
    games = []
    prev = s[0]
    cnt = 1
    for i in range(1, n):
        if s[i] == prev:
            cnt += 1
        else:
            games.append((prev, cnt))
            prev = s[i]
            cnt = 1
    games.append((prev, cnt))
    if diff > 0:
        return n
    else:
        not_in = 0
        for game in games:        
            if diff > 0:
                return n - not_in
            elif diff <= 0 and game[0] == '2':
                not_in += game[1]
            else:
                diff += D * game[1]
    return n - not_in


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        R0, X, D, n = map(int, input().split())
        s = input().strip()
        print(solve(R0, X, D, n, s))