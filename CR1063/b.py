from collections import defaultdict
def solve(n, arr, x):
    if x[0] == '1' or x[-1] == '1':
        return -1
    visited_max = arr[0]
    visited_min = arr[0]
    unvisited_max = n+1 if x[0] != n+1 else n
    unvisited_min = 1 if x[0] != 1 else 2 
    indexes = defaultdict(int)
    indexes[arr[0]] = 1
    indexes[arr[-1]] = n+1
    ans = defaultdict(list)
    for i in range(1, n - 1):
        indexes[arr[i]] = i+1
        if x[i] == '1':
            if arr[i] == 1 or arr[i] == n:
                return -1
            if visited_min < arr[i] < unvisited_max:
                ans[i] = (visited_min, unvisited_max)
            elif unvisited_min < arr[i] < visited_max:
                ans[i] = (unvisited_min, visited_max)
    for key, values in ans.items():
        pair1, pair2 = values
            
            
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        x = input()
        print(solve(n, arr, x))
        