from collections import Counter

def solve(s):
    counter = Counter(s)
    sm = counter['0'] + counter['1']
    for i in range(sm):
        if counter['1' if s[i] == '0' else '0'] == 0:
            print(sm - i)
            return
        else:
            oppo = '1' if s[i] == '0' else '0'
            counter[oppo] -= 1
    print(0)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        solve(s)