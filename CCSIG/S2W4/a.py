def solve():
    blank = input().strip()
    grid = [input().strip() for _ in range(8)]
    
    for row in grid:
        if row == "R" * 8:
            print("R")
            return
    
    print("B")
    return
        
            


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()

