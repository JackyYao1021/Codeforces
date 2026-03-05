from collections import Counter
def solve(n, arr):
    z = arr.count(0)

    wrong_z_idx = []
    wrong_o_idx = []
    for i in range(z):
        if arr[i] == 1:
            wrong_o_idx.append(i + 1)
    for i in range(z, n):
        if arr[i] == 0:
            wrong_z_idx.append(i + 1)
    
    wrong_idx = wrong_z_idx + wrong_o_idx

    if not wrong_idx:
        print("Bob")
        return

    print("Alice")
    print(len(wrong_idx))
    print(" ".join(map(str, sorted(wrong_idx))))
    
    
        
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input()))
        solve(n, arr)