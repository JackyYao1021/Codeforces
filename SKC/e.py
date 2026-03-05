def solve(n, arr, k):
    cnts = [0] * k
    new = [arr[0]]
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            new.append(arr[i])
            
    cnts[new[0]-1] += 1
    cnts[new[-1]-1] += 1
    
    for i in range(1, len(new)-1):
        if new[i-1] != new[i+1]:
            cnts[new[i]-1] += 1
        else:
            cnts[new[i]-1] += 2
    ans = 1
    tmp = 0
    for i, cnt in enumerate(cnts):
        if cnt > tmp:
            ans = i + 1
            tmp = cnt
    return ans
    

if __name__ == "__main__":
    n, k = map(int,  input().split())
    arr = list(map(int, input().split()))
    print(solve(n, arr, k))
    
    