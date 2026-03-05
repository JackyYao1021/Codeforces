def solve(n, arr):
    sorted_arr = sorted(arr)
    not_sorted = set()
    
    if sorted_arr == arr:
        print(-1)
        return
    
    for i in range(n):
        if sorted_arr[i] != arr[i]:
            not_sorted.add(arr[i])
            
    
    max_val = max(arr)
    min_val = min(arr)
    if not_sorted == {max_val, min_val}:
        print(max_val - min_val)
        return
    
    ans = float('inf')
    for val in list(not_sorted):
        ans = min(ans, max(val - min_val, max_val - val))
    print(ans)
    
    

    
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)