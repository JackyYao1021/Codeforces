def solve(n, k, arr, brr):
    if k == 1:
        for i in range(n):
            if brr[i] != -1 and brr[i] != arr[i]:
                print("NO")
                return
        print("YES")
        return
    
    for i in range(k):
        group_a = [arr[j] for j in range(i, n, k)]
        group_b = [brr[j] for j in range(i, n, k)]
        if len(set(group_a)) == 1:
            set_b = set(group_b)
            if len(set_b) > 2:
                print("NO")
                return
            if len(set_b) == 2 and -1 not in set_b:
                print("NO")
                return
        else:
            if group_a != group_b:
                print("NO")
                return
    print("YES")
            

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        solve(n, k, arr, brr)