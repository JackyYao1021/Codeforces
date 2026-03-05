import heapq

days = int(input())
snacks = list(map(int, input().split()))

index = days

heap = []

for i in range(days):
    snack = snacks[i]
    if snack == index:
        tmp = [snack]
        index -= 1
        while heap and heap[0] == -index:
            tmp.append(-heapq.heappop(heap))
            index -= 1
        print(*tmp)
    else:
        heapq.heappush(heap, -snack)
        print()
