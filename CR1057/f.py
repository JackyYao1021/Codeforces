from collections import Counter
ans = [0]

def solve(table, x_prime, y_prime, n):
    x =(x_prime - 1 + ans[-1]) % n +1
    y =(y_prime - 1 + ans[-1]) % n +1
    
    l, r = min(x, y), max(x, y)
    result_set = table[r] ^ table[l-1]
    tmp_ans = sum(result_set)
    ans.append(tmp_ans)
    return tmp_ans



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        arr = list(map(int, input().split()))
        table = {0: set()}
        for i in range(1, n+1):
            if arr[i-1] not in table[i-1]:
                table[i] = table[i-1].copy()
                table[i].add(arr[i-1])
            else:
                table[i] = table[i-1].copy()
                table[i].remove(arr[i-1])
        ans = [0]
        
        for _ in range(q):    
            x_prime, y_prime = map(int, input().split())
            res = solve(table, x_prime, y_prime, n)
        print(*ans[1:])