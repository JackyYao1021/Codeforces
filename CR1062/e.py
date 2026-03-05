from heapq import heappop, heappush
def solve(n, k, x, arr):
    ans = set()
    arr.sort()
    arr.insert(0, -arr[0])
    arr.append(2*x - arr[-1])
    n = len(arr)
    
    hp = []
    for i in range(n - 1):
        diff = arr[i+1] - arr[i]
        if diff % 2 == 0:
            heappush(hp, (-(diff//2), [(arr[i] + arr[i+1])//2]))
        else:
            mid = (arr[i] + arr[i+1])//2
            heappush(hp, (-(diff//2), [mid, mid +1]))
    
    while k > 0:
        diff, places = heappop(hp)
        for place in places:
            if k == 0:
                break
            if place not in ans:
                ans.add(place)
                k -= 1
                new_places = []
                if diff > 0:
                    continue
                if place - 1 >= 0 and (place - 1) not in ans:
                    new_places.append(place - 1)
                if place + 1 <= x and (place + 1) not in ans:
                    new_places.append(place + 1)
                heappush(hp, (diff+1, new_places))

    sorted_ans = list(ans)
    return sorted_ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        arr = list(map(int, input().split()))
        print(*solve(n, k, x, arr))