def prime_factorise(n):
    i = 2
    factors = []
    while i * i <= n:
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return set(factors)

def solve(a_list, b_list):
    a_factors = []
    a_plus_factors = []
    for a in a_list:
        a_factors.append(prime_factorise(a))
        a_plus_factors.append(prime_factorise(a+1))
    
    find_one = False
    for i in range(len(a_list)):
        for j in range(len(a_list)):
            if i == j:
                continue
            if len(a_factors[i].intersection(a_factors[j])) > 0:
                return 0
            if len(a_factors[i].intersection(a_plus_factors[j])) > 0:
                find_one = True
    if find_one:
        return 1
    return 2
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        t = int(input())
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
        print(solve(a_list, b_list))