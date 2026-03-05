import sys
from collections import Counter

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.sum = 0

def update(prev_node, start, end, idx, val):
    new_node = Node()
    
    if prev_node:
        new_node.left = prev_node.left
        new_node.right = prev_node.right
        new_node.sum = prev_node.sum

    if start == end:
        new_node.sum = val
        return new_node

    mid = (start + end) // 2
    
    if idx <= mid:
        new_node.left = update(prev_node.left if prev_node else None, start, mid, idx, val)
    else:
        new_node.right = update(prev_node.right if prev_node else None, mid + 1, end, idx, val)

    sum_left = new_node.left.sum if new_node.left else 0
    sum_right = new_node.right.sum if new_node.right else 0
    new_node.sum = sum_left + sum_right
    
    return new_node

def query_intersection(node1, node2, start, end):
    
    if not node1 or not node2 or node1.sum == 0 or node2.sum == 0:
        return 0

    if start == end:
        return node1.sum

    mid = (start + end) // 2
    
    left_intersect_sum = query_intersection(node1.left, node2.left, start, mid)
    right_intersect_sum = query_intersection(node1.right, node2.right, mid + 1, end)
    
    return left_intersect_sum + right_intersect_sum

def solve():
    n, q = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    unique_vals = sorted(list(set(arr)))
    val_to_idx = {val: i for i, val in enumerate(unique_vals)}
    m = len(unique_vals)

    roots = [None] * (n + 1)
    counts = Counter()

    for i in range(n):
        val = arr[i]
        val_idx = val_to_idx[val]
        counts[val] += 1
        
        new_leaf_val = 0
        if counts[val] % 2 == 1:
            new_leaf_val = val
        
        roots[i+1] = update(roots[i], 0, m - 1, val_idx, new_leaf_val)

    ans_list = [0]
    final_results = []

    for _ in range(q):
        x_prime, y_prime = map(int, sys.stdin.readline().split())
        
        last_ans = ans_list[-1]
        x = (x_prime - 1 + last_ans) % n + 1
        y = (y_prime - 1 + last_ans) % n + 1
        
        l, r = min(x, y), max(x, y)

        root_r = roots[r]
        root_l = roots[l - 1]

        sum_r = root_r.sum if root_r else 0
        sum_l = root_l.sum if root_l else 0
        
        sum_intersect = query_intersection(root_r, root_l, 0, m - 1)

        current_ans = sum_r + sum_l - (2 * sum_intersect)
        ans_list.append(current_ans)
        final_results.append(str(current_ans))

    print(" ".join(final_results))

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()