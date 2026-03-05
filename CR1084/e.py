def divisors(n):
    if n == 1:
        return 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i    
            if n != 1:
                return 0
            else:
                return i
    return n
            
def solve(n, arr):
    tmp = arr[0]
    flag = True
    for i in range(1, len(arr)):
        if arr[i] < tmp:
            flag = False
            break
        tmp = arr[i]

    if flag:
        print("Bob")
        return
    
    
    for idx, a in enumerate(arr):
        tmp = divisors(a)
        if tmp == 0:
            print("Alice")
            return 
        else:
            arr[idx] = tmp
    tmp = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < tmp:
            print("Alice")
            return
        tmp = arr[i]
    
    print("Bob")
            
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(n, arr)