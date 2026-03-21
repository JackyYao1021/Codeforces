def solve(n, s):
    for i, c in enumerate(s):
        if c == 'L':
            print(i+1)
            return 
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        solve(n, s)