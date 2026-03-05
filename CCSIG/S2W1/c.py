def solve(n, k, arr):
    if k == 2:
        ans = 1
        for a in arr:
            if a % 2 == 0:
                ans = 0
                print(ans)
                return
        print(ans)
    elif k == 3:
        ans = 0
        for a in arr:
            if a % 3 == 0:
                print(0)
                return
            ans = max(ans,a%3)
        print(k-ans)
    elif k == 4:
        cnts = [0]*4
        for a in arr:
            cnts[a % 4] += 1
        if cnts[0] > 0:
            print(0)
            return
        if cnts[2] > 1:
            print(0)
            return
        if cnts[3] > 0:
            print(1)
            return
        if cnts[2] == 1:
            print(1)
            return
        else:
            print(2)
            
    elif k == 5:
        ans = 0
        for a in arr:
            if a % 5 == 0:
                print(0)
                return
            ans = max(ans,a%5)
        print(k-ans)
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, k, arr)