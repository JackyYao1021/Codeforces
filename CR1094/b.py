def solve(n, m, arr, pos):
    odd_list = []
    even_list = []
    for i in range(n):
        if i % 2 == 1:
            even_list.append(arr[i])
        else:
            odd_list.append(arr[i])
    
    odd_list.sort(reverse=True)
    even_list.sort(reverse=True)
    
    tmp = 0
    odd_idx = 0
    even_idx = 0
    for p in pos:
        if p % 2 == 0 and even_idx < len(even_list) and (even_idx == 0 or even_list[even_idx] > 0):                
            tmp += even_list[even_idx]
            even_idx += 1
        elif p % 2 == 1 and odd_idx < len(odd_list) and (odd_idx == 0 or odd_list[odd_idx] > 0):
            tmp += odd_list[odd_idx]
            odd_idx += 1
    print(sum(arr) - tmp)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        pos = list(map(int, input().split()))
        solve(n, m, arr, pos)