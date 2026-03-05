def solve(n, s):
    
    if s.count(s[0]) == n:
        print(1)
        return
    
    num_change = 0
    continous = False
    
    for i in range(n):
        if s[i] != s[i-1]:
            num_change += 1
        else:
            continous = True

    if continous:
        print(num_change+1)
        return

    print(num_change)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        solve(n, s)