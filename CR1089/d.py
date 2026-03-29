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


# def ahu(tree, u):
    


def solve(n, a, b):
    tree_a = build_tree(a)
    tree_b = build_tree(b)
    
    print(tree_a)
    print(tree_b)
    
    # label_a = ahu(tree_a, 0)
    # label_b = ahu(tree_b, 0)
    # print(label_a)
    # print(label_b)
    # if label_a == label_b:
    #     print("YES")
    # else:
    #     print("NO")
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input()
        b = input()
        solve(n, a, b)