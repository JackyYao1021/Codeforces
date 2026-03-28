def solve(s):
    ans = []
    ans.append(s[0].upper())
    for c in s[1:]:
        ans.append(c)

    print("".join(ans))        

if __name__ == "__main__":
    s = input()
    solve(s)