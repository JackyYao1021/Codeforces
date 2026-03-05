
def solve(n, arr):
    ans = ""
    for n in arr:
        tmp1 = n+ans
        tmp2 = ans+n
        if add_left(tmp1, tmp2):
            ans = tmp1
        else:
            ans = tmp2
    return ans
        
        
    

def add_left(a, b):
    for i in range(len(a)):
        if a[i] < b[i]:
            return True
        elif a[i] > b[i]:
            return False
        i += 1 

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(input().split())
        print(solve(n, arr))