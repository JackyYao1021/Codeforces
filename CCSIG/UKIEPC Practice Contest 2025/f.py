def solve(arr):
    team_a = arr[0][0]
    team_b = arr[0][1]
    for (a, b) in arr[1:]:
        if a == team_a and b > team_b:
            team_b = b
        elif a > team_a and b == team_b:
            team_a = a
        elif a > team_a and b > team_b:
            team_a = a
            team_b = b
        else:
            return "no"
    return "yes"

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(tuple(map(int, input().split())))
    print(solve(arr))
    
    