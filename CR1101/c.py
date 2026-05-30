def following_E(idx, u):
    cnt = 0
    for i in range(idx + 1, len(u)):
        if u[i] == "E":
            cnt += 1
        else:
            break
    return cnt

def solve():
    n, x, s = map(int, input().split())
    u = input()
    ans = 0
    empty_for_E = 0
    cnt_i = u.count("I")
    
    for idx, c in enumerate(u):
        if c == "I":
            if x > 0:
                x -= 1
                ans += 1
                empty_for_E += s - 1
                cnt_i -= 1
        elif c == "E":
            if empty_for_E > 0:
                ans += 1
                empty_for_E -= 1
        elif c == "A":
            cnt_E = following_E(idx, u)
            if cnt_i < x:
                x -= 1
                ans += 1
                empty_for_E += s - 1
            elif cnt_E + 1 > empty_for_E:
                if x > 0:
                    x -= 1
                    ans += 1
                    empty_for_E += s - 1
            else:
                ans += 1
                empty_for_E -= 1
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()