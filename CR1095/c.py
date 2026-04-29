from collections import Counter
    
def solve(n, arr):
    left = 0
    right = n + 1
    counter = Counter(arr)

    def check(k):
        tmp_counter = counter.copy()
        mx_pointer = max(arr)

        for i in range(k - 1, -1, -1):
            if tmp_counter[i] > 0:
                tmp_counter[i] -= 1
                continue

            while mx_pointer >= 0 and tmp_counter[mx_pointer] == 0:
                mx_pointer -= 1

            if mx_pointer > 2 * i:
                tmp_counter[mx_pointer] -= 1
                continue
            else:
                return False

        return True
        
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid            
        
    print(left - 1)
    
    
            
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)