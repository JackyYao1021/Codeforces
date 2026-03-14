from collections import defaultdict
def solve(n, tasks):
    mem = defaultdict(int)
    mem[0] = 1
    for c, p in tasks:
        for c_old, p_old in list(mem.items()):
            if c_old <= c and p_old <= p:
                mem[c] = max(mem[c], p)

    print(mem[0])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        tasks = []
        for _ in range(n):
            tasks.append(list(map(int, input().split())))
        solve(n, tasks)
        