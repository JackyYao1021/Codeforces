from collections import defaultdict
from heapq import heappush, heappop, nlargest
def solve(n, m, particles, shops):
    dic = defaultdict(list)
    for i in range(n):
        x, y = particles[i]
        dic[y].append(x)
    
    rest_values = defaultdict(int)
    
    mx = 0
    heap = []
    
    for key, values in dic.items():
        for v in values:
            heappush(heap, v)
        if len(heap) >= key:
            if len(heap) >= key+1:
                largest_values = nlargest(key+1, heap)
                sum_values = sum(largest_values)
                mx = max(mx, sum_values)
                rest_values[key] = sum_values - largest_values[-1]
            else:
                sum_values = sum(nlargest(key, heap))
                rest_values[key] = sum_values
        
    ans = []                
    for new_particles in shops:
        x, y = new_particles
        if y in rest_values:
            ans.append(max(mx, rest_values[y]+x))
        else:
            ans.append(mx)
    print(*ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        particles = []
        for _ in range(n):
            x, y = map(int, input().split())
            particles.append((x, y))
        
        shops = []
        for _ in range(m):
            x, y = map(int, input().split())
            shops.append((x, y))
            
        solve(n, m, particles, shops)
        