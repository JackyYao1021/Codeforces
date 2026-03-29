def parse_blocks(s):
    blocks = []
    bal = 0
    start = 0
    for i, ch in enumerate(s):
        if ch == '(':
            bal += 1
        else:
            bal -= 1
        if bal == 0:
            blocks.append(s[start:i+1])
            start = i + 1
    return blocks

def build_expr(s):
    blocks = parse_blocks(s)
    res = []
    for blk in blocks:
        inner = blk[1:-1]
        if inner == "":
            res.append([])
        else:
            res.append(build_expr(inner))
    return res

def build_tree(a):
    children = [[]]
    
    stack = [0]
    for c in a:
        if c == '(':
            node_id = len(children)
            children.append([])
            children[stack[-1]].append(node_id)
            stack.append(node_id)
        else:
            stack.pop()
    return children


def ahu(tree, u):
    labels = []
    for v in tree[u]:
        labels.append(ahu(tree, v))
    labels.sort()
    return "(" + "".join(labels) + ")"


def solve(n, a, b):
    # a = "(" + a + ")"
    # b = "(" + b + ")"

    blocks_a = parse_blocks(a)
    blocks_b = parse_blocks(b)

    print(blocks_a)
    print(blocks_b)
    
    # label_a = ahu(tree_a, 0)
    # label_b = ahu(tree_b, 0)

    # if label_a == label_b:
    #     print("YES")
    # else:
    #     print("NO")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().strip()
        b = input().strip()
        solve(n, a, b)