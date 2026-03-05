def solve(n, arr):
    mx = []
    mn = []
    know_max = False
    
    for i in range(n):
        if know_max:
            if arr[i] == '1':
                mx.append(0)
                mn.append(1)
            elif arr[i] == '2':
                mx.append(0)
                mn.append(2)
            else:
                mx.append(0)
                mn.append(0)
        else:
            if arr[i] == '1':
                mx.append(1)
                mn.append(0)
                know_max = True
            elif arr[i] == '2':
                mx.append(1)
                mn.append(1)
            else:
                mx.append(0)
                mn.append(0)
    
    print("".join(map(str, mx)))
    print("".join(map(str, mn)))
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().strip()
        solve(n, arr)