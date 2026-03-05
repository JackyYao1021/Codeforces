from bisect import bisect_right

def solve(n, m, arr, brr):
    buildings = [0] * (n+1)
    buildings[0] = 1
    for i in range(1, n+1):
        buildings[i] = buildings[i-1] + arr[i-1]
    
    
    for b in brr:
        building_idx = bisect_right(buildings, b)
        room_idx = b - buildings[building_idx-1] + 1
        print(f"{building_idx} {room_idx}")
        
        





if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    solve(n, m, arr, brr)
        