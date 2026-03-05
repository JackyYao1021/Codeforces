from collections import defaultdict, Counter
import heapq



if __name__ == "__main__":
    n, m, r = map(int, input().split())
    solved = defaultdict(set)
    pending = set(range(1, n + 1))
    
    for i in range(1, n + 1):
        result = list(map(int, input().split()))
        counter = Counter(result)
        solved[counter["A"]].add(i)
        
        