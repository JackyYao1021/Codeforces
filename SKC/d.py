from bisect import bisect_left, bisect_right

def solve(n, arr):
    even_cnt = 0
    odd_cnt = 0
    max_even = -1
    max_odd = -1
    evens = []
    for a in arr:
        if a % 2 == 0:
            even_cnt += 1
            if a > max_even:
                max_even = a
            evens.append(a)
        else:
            odd_cnt += 1
            if a > max_odd:
                max_odd = a
    if even_cnt == 0 or odd_cnt == 0:
        return 0
    
    if max_even < max_odd:
        return even_cnt
    else:
        evens.sort()
        mx = max_odd
        for a in evens:
            if a < mx:
                mx += a
            else:
                return even_cnt + 1
        return even_cnt
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(n, arr))