def check_palindrome(arr, i, j):
    left = i
    right = j
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def mex(arr):
    s = set(arr)
    for i in range(len(arr) + 1):
        if i not in s:
            return i

def check(arr, i, j):
    if i == j + 1:
        left = i
        right = j
        while left >= 0 and right < len(arr):
            if arr[left] == arr[right]:
                left -= 1
                right += 1
            else:
                break
        return mex(arr[left + 1:right])
    else:
        left1 = i
        right1 = i
        while left1 >= 0 and right1 < len(arr):
            if arr[left1] == arr[right1]:
                left1 -= 1
                right1 += 1
            else:
                break
        left2 = j
        right2 = j
        while left2 >= 0 and right2 < len(arr):
            if arr[left2] == arr[right2]:
                left2 -= 1
                right2 += 1
            else:
                break
            
        ans = max(mex(arr[left1 + 1:right1]), mex(arr[left2 + 1:right2]))
        
        if check_palindrome(arr, i, j):
            left = i
            right = j
            while left >= 0 and right < len(arr):
                if arr[left] == arr[right]:
                    left -= 1
                    right += 1
                else:
                    break
            ans = max(ans, mex(arr[left + 1:right]))
    
        return ans 
        
        

def solve(n, arr):
    ans = 1
    idx1 = -1
    idx2 = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            if idx1 == -1:
                idx1 = i
            else:
                idx2 = i
                break
    ans = check(arr, idx1, idx2)
    print(ans)
     
        
        
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        solve(n, arr)