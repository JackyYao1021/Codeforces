from collections import Counter
def solve(n, arr):
    left = 0
    right = 0
    
    for a in arr:
        if a == "(":
            left += 1
        elif a == ")":
            right += 1
    if left == right:
        print("YES")
    else:
        print("NO")    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input()
        solve(n, arr)
        