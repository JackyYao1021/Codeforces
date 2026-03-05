def solve(s):
    indexes = [i+1 for i, ch in enumerate(s) if ch == '0']
    print(len(indexes))
    print(*indexes)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input()
        solve(arr)