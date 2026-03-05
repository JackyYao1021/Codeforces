def solve(n, arr):
    lst = arr[-1]
    fst = arr[0]
    if lst != "-1" and fst != "-1":
        print(abs(int(lst) - int(fst)))
        print(*[a if a != "-1" else "0" for a in arr ])
    elif lst == "-1" and fst == "-1":
        print(0)
        print(*[a if a != "-1" else "0" for a in arr ])
    elif lst == "-1":
        arr[-1] = fst
        print(0)
        print(*[a if a != "-1" else "0" for a in arr])
    else:
        print(0)
        arr[0] = lst
        print(*[a if a != "-1" else "0" for a in arr])
        
        
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(input().split())
        solve(n, arr)