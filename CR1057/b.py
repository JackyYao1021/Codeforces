def solve(x, y, z):
    while x > 0 or y > 0 or z > 0:
        if x > 0:
            l_x = x & 1
            x >>= 1
        else:
            l_x = 0
        if y > 0:    
            l_y = y & 1
            y >>= 1
        else:
            l_y = 0
        if z > 0:
            l_z = z & 1 
            z >>= 1
        else:
            l_z = 0
        
        if l_x + l_y + l_z == 2:
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y, z = map(int, input().split())
        print(solve(x, y, z))