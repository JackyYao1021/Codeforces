def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 3 -> 1 
    # 2 -> 0 -> 2
    # 5, 3, 1
    even_group_0 = 0
    even_group_1 = 0
    odd = 0
    
    
    for i in range(n):
        if arr[i] % 2 == 0:
            if arr[i] % 4 == 0:
                even_group_0 += 1
            else:
                even_group_1 += 1
        else:
            odd += 1
            
    print(max(odd, even_group_0, even_group_1))
    
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()