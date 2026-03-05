def solve(n, x, y, arr):
    x_diff = abs(x)
    y_diff = abs(y)
    
    for a in arr:
        if a == '4':
            if x_diff > y_diff:
                x_diff -= 1
            else:
                y_diff -= 1
        elif a == '8':
            x_diff -= 1
            y_diff -= 1
    
    if x_diff <= 0 and y_diff <= 0:
        print("YES")
    else:
        print("NO")
        
        
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x, y = map(int, input().split())
        arr = input()
        solve(n, x, y, arr)