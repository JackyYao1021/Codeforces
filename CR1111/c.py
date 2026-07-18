def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    zero_to_one = 0
    one_to_zero = 0
    one_to_one = 0
    zero_to_zero = 0
    
    
    for i in range(n):
        if arr[i] == 0 and brr[i] == 1:
            zero_to_one += 1
        elif arr[i] == 1 and brr[i] == 0:
            one_to_zero += 1
        elif arr[i] == 1 and brr[i] == 1:
            one_to_one += 1
        else:
            zero_to_zero += 1
            
    if one_to_zero == 0 and zero_to_one == 0:
        print(0)
        return
    if one_to_zero == 0 and zero_to_one > 0:
        if one_to_one > 0 and zero_to_zero > 0:
            print(2)
            return
        else:
            print(-1)
            return
    if one_to_zero % 2 == 0:
        print(2)
    else:
        print(1)
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
        