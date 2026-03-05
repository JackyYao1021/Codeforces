def solve(s):
    cnt_a = s.count('A')
    cnt_b = s.count('B')
    return 'A' if cnt_a > cnt_b else 'B' 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(solve(s))