def solve(s):
    def cost(positions):
        if not positions: return float('inf')
        k = len(positions)
        median_index = k // 2
        base = positions[median_index] - median_index
        return sum(abs(positions[i] - (base + i)) for i in range(k))

    pos_a = [i for i, ch in enumerate(s) if ch == 'a']
    pos_b = [i for i, ch in enumerate(s) if ch == 'b']
    return min(cost(pos_a), cost(pos_b))

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    print(solve(s))