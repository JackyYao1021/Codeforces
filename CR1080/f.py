from collections import deque

def solve(n, parameters):
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            a1, b1, c1, = parameters[i]
            a2, b2, c2 = parameters[j]
            if (b1 - b2) ** 2 - 4 * (a1 - a2) * (c1 - c2) < 0:
                edges.append((i, j))
            if a1 == a2 and b1 == b2 and c1 != c2:
                edges.append((i, j))

        
    




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        parameters = []
        for _ in range(n):
            parameters.append(list(map(int, input().split())))
        solve(n, parameters)