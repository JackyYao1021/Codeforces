def print_ans(mx, mid, mn, mx_char, mid_char, mn_char):
    if mid == 0:
        print(mx_char)
        return
    
    base = (mx_char + mid_char) * mid
    mx -= mid
    if mn == 0:
        if mx > 0:
            ans = base + mx_char
        else:
            ans = base
        print(ans)
        return
    
    if mx > mn:
        append = (mx_char + mn_char) * mn + mx_char
        ans = base + append
        print(ans)
        return
    elif mx == mn:
        append = (mx_char + mn_char) * mx
        ans = append + base
        print(ans)
        return
    else:
        append = (mx_char + mn_char) * mx
        ans = append + base + mn_char
        print(ans)
        return
    
def solve(r, g, b):
    mx = max(r, g, b)
    if r == g and r == mx:
        print_ans_2(r, g, b, "R", "G", "B")
        return 
    if g == b and g == mx:    
        print_ans_2(g, b, r, "G", "B", "R")
        return 
    if r == b and r == mx:
        print_ans_2(r, g, b, "R", "G", "B")
        return
    
    mn = min(r, g, b)
    if r == mx:
        if g == mn:
            print_ans(r, b, g, "R", "B", "G")
            return     
        else:
            print_ans(r, g, b, "R", "G", "B")
            return
    elif g == mx:
        if r == mn:
            print_ans(g, b, r, "G", "B", "R")
            return     
        else:
            print_ans(g, r, b, "G", "R", "B")
            return
    elif b == mx:
        if r == mn:
            print_ans(b, g, r, "B", "G", "R")
            return     
        else:
            print_ans(b, r, g, "B", "R", "G")
            return
    
def print_ans_2(mx, mid, mn, mx_char, mid_char, mn_char):
    
    base = (mx_char+mid_char) * mx
    # base = "RG" * (r)
    if mn == 0:
        ans = base
    elif mn == 1:
        ans = base + mn_char
    else:
        ans = mn_char + base + mn_char
    print(ans)
    return 
    
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        r, g, b = map(int, input().split())
        solve(r, g, b)