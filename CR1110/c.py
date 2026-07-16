

def solve():
    n, k = map(int, input().split())
    mx_len = n.bit_length()
    # if k > 2 ** mx_len - 1:
    #     print("NO")
    #     return
    
    mask = n ^ k
    
    mx_len = (n-1).bit_length()
    if mask > 2 ** mx_len - 1:
        print("NO")
        return  
        
    removed = []
    power = 0
    while mask > 0:
        lst = mask & 1
        if lst == 1:
            removed.append(2 ** power)
        mask >>= 1
        power += 1
    ans = []
    for i in range(n-1, -1, -1):
        if i not in removed:
            ans.append(i)
    
    for x in removed:
        ans.append(x)
    print("YES")
    print(" ".join(map(str, ans)))



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        