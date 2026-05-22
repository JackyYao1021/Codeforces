from bisect import bisect_left, bisect_right

def build_max(length, digits):
    mx_digit = digits[-1]
    mn_digit = digits[0]
    return str(mx_digit) * length

def build_min(length, digits):
    mx_digit = digits[-1]
    mn_digit = digits[0]
    if mn_digit == 0:
        if length == 1:
            return '0'
        else:
            return str(digits[1]) + str(mn_digit) * (length - 1)
    else:
        return str(mn_digit) * length
    
def smaller_equal(a, digits):
    m = len(a)
    tmp = []
    for i, ch in enumerate(a):
        digit = int(ch)
        idx = bisect_right(digits, digit) - 1

        if idx >= 0:
            chosen = digits[idx]

            if chosen == digit:
                tmp.append(chosen)
                continue

            tmp.append(chosen)
            tmp.extend([max(digits)] * (m - i - 1))
            return ''.join(map(str, tmp))

        for j in range(i - 1, -1, -1):
            prev = tmp[j]

            idx = bisect_left(digits, digit) - 1

            if idx >= 0:
                tmp[j] = digit[idx]
                tmp = tmp[:j + 1]
                tmp.extend([max(digits)] * (m - j - 1))
                return ''.join(map(str, tmp))

        return build_max(m - 1, digits)

    return ''.join(map(str, tmp))

def greater_equal(a, digits):
    m = len(a)
    tmp = []
    for i, ch in enumerate(a):
        digit = int(ch)
        idx = bisect_left(digits, digit)

        if idx < len(digits):
            chosen = digits[idx]

            if chosen == digit:
                tmp.append(chosen)
                continue

            tmp.append(chosen)
            tmp.extend([min(digits)] * (m - i - 1))
            return ''.join(map(str, tmp))

        for j in range(i - 1, -1, -1):
            prev = tmp[j]

            idx = bisect_right(digits, digit)

            if idx >= 0:
                tmp[j] = digits[idx]
                tmp = tmp[:j + 1]
                tmp.extend([min(digits)] * (m - j - 1))
                return ''.join(map(str, tmp))

        return build_min(m + 1, digits)

    return ''.join(map(str, tmp))
            
def solve(a, n, digits):
    a = str(a)
    a_length = len(a)
    
    smaller = smaller_equal(a, digits)
    larger = greater_equal(a, digits)
    
    candidates = []
    if smaller is not None:
        candidates.append(smaller)
    if larger is not None:
        candidates.append(larger)
    
    ans = float('inf')
    for c in candidates:
        ans = min(ans, abs(int(c) - int(a)))
    print(ans)
      

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, n = map(int, input().split())
        digits = list(map(int, input().split()))
        solve(a, n, digits)