def solve(n, arr):
    fst = -1
    for i in range(n):
        if arr[i] == n:
            n -= 1
        else:
            fst = i
            break
    
    if n == 0:
        print(" ".join(map(str, arr)))
        return
    else:
        idx = arr.index(n)
        reversed_part = arr[fst:idx+1]
        reversed_part.reverse()
        result = arr[:fst] + reversed_part + arr[idx+1:]
        print(" ".join(map(str, result)))
    
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)
        
        