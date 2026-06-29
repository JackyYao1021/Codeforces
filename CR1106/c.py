from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    children = defaultdict(list)

    for i in range(n - 1):
        children[arr[i]].append(i + 2)

    value = [1] * (n + 1)
    depth = [1] * (n + 1)

    stack = [1]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)
        for child in children[node]:
            stack.append(child)

    for node in reversed(order):
        largest = 0
        second_largest = 0
        for child in children[node]:
            value[node] += value[child]
            child_depth = depth[child]

            if child_depth > largest:
                second_largest = largest
                largest = child_depth
            elif child_depth > second_largest:
                second_largest = child_depth

        depth[node] = largest + 1
        value[node] += second_largest

    print(value[1])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()