from bisect import bisect_left, bisect_right

def solve(a, n, digits):
    a_copy = a
    mx_digit = max(digits)
    mn_digit = min(digits)
    
    if mx_digit == 0 and mn_digit == 0:
        print(a)
        return
    
    a_length = len(str(a))
    a_digits = []
    if a == 0:
        a_digits.append(0)
    while a > 0:
        a_digits.append(a % 10)
        a //= 10
        
    b = 0
    
    a_digits.reverse()
    # print(a_digits)
    for i in range(a_length):
        if a_digits[i] in digits:
            b = b * 10 + a_digits[i]
        else:
            smaller_tmp = -1
            smaller_digit = bisect_left(digits, a_digits[i]) - 1
            if smaller_digit >= 0:
                smaller_tmp = b * 10 + digits[smaller_digit]
                for j in range(i + 1, a_length):
                    smaller_tmp = smaller_tmp * 10 + mx_digit
                
            
            larger_digit = bisect_right(digits, a_digits[i])
            larger_tmp = -1
            if larger_digit < len(digits):
                larger_tmp = b * 10 + digits[larger_digit]
                for j in range(i + 1, a_length):
                    larger_tmp = larger_tmp * 10 + mn_digit
                
            if smaller_tmp == -1 and larger_tmp == -1:
                break
            if smaller_tmp == -1:
                b = larger_tmp
                break
            if larger_tmp == -1:
                b = smaller_tmp
                break
            if abs(a_copy - smaller_tmp) <= abs(a_copy - larger_tmp):
                b = smaller_tmp
                break
            else:
                b = larger_tmp
                break
    
    if mn_digit != 0:
        longer_tmp = mn_digit
        for i in range(a_length):
            longer_tmp = longer_tmp * 10 + mn_digit
    else:
        # mx == 0 been remove at the top
        snd = bisect_right(digits, 0)
        longer_tmp = digits[snd]
        for i in range(a_length):
            longer_tmp = longer_tmp * 10 + mn_digit
    
    # mx == 0 been remove at the top
    shorter_tmp = mx_digit
    for i in range(a_length - 2):
        shorter_tmp = shorter_tmp * 10 + mx_digit
        
    candidates = [b, longer_tmp, shorter_tmp]
    mn_diff = float("inf")
    for c in candidates:
        diff = abs(c - a_copy)
        if diff < mn_diff:
            mn_diff = diff
    print(mn_diff)        
    
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, n = map(int, input().split())
        digits = list(map(int, input().split()))
        solve(a, n, digits)