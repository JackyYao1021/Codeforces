def solve(n, arr, adj, m):
    ans = 0
    stack = [(0, -1, 0)]

    while stack:
        u, parent, cnt = stack.pop()

        if arr[u] == 1:
            cnt += 1
        else:
            cnt = 0

        if cnt > m:
            continue

        is_leaf = True
        for v in adj[u]:
            if v == parent:
                continue
            is_leaf = False
            stack.append((v, u, cnt))

        if is_leaf:
            ans += 1

    print(ans)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    solve(n, arr, adj, m)