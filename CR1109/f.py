from collections import deque


def solve():
    n = int(input())

    parents = [0] + list(map(int, input().split()))
    ids = list(map(int, input().split()))

    children = [[] for _ in range(n)]

    for node in range(1, n):
        parent = parents[node] - 1
        children[parent].append(node)

    queue = deque([0])
    bfs_order = []

    while queue:
        node = queue.popleft()
        bfs_order.append(node)

        for child in children[node]:
            queue.append(child)

    ranges = [[0, 0] for _ in range(n)]
    leave_cnt = [0] * n

    for node in reversed(bfs_order):
        if ids[node] != 0:
            ranges[node] = [ids[node], ids[node]]
            leave_cnt[node] = 1
            continue
    
        min_id = float('inf')
        max_id = float('-inf')

        for child in children[node]:
            leave_cnt[node] += leave_cnt[child]
            left, right = ranges[child]
            min_id = min(min_id, left)
            max_id = max(max_id, right)

        if leave_cnt[node] != max_id - min_id + 1:
            print("NO")
            return
        
        child_list = children[node]
        child_cnt = len(child_list)

        for i in range(child_cnt):
            current_child = child_list[i]
            next_child = child_list[(i + 1) % child_cnt]

            current_right = ranges[current_child][1]
            next_left = ranges[next_child][0]

            if current_right == max_id:
                expected_left = min_id
            else:
                expected_left = current_right + 1

            if next_left != expected_left:
                print("NO")
                return
                
        ranges[node] = [min_id, max_id]
    print("YES")



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()