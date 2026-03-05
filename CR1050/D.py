t = int(input())
for _ in range(t):
    n = int(input())
    dandelions = list(map(int, input().split()))
    even = 0
    odd = []
    for d in dandelions:
        if d % 2 == 0:
            even += d
        else:
            odd.append(d)
    if len(odd) == 0:
        print(0)
    else:
        odd.sort(reverse=True)
        even += sum(odd[:(len(odd) // 2) + (len(odd) % 2)])
        print(even)