def ask_question(idx, n):
    print(f"? {idx} {n}", flush=True)
    response = int(input())
    return response

def helper(idx_list, reminder, divider, n):
    if n == 0:
        if reminder == 0:
            return 1 << divider
        else:
            return reminder
    
    if divider == 0:
        q = 1 << divider
    else:
        q = (1 << divider) ^ (((1<<divider)-1) ^ reminder)

    even = (len(idx_list) + 1) // 2
    odd_list = []
    even_list = []
    for i in idx_list:
        result = ask_question(i, q)
        if result == 1:
            odd_list.append(i)
        else:
            even_list.append(i)

    if len(even_list) < even:
        idx_list = even_list
        divider += 1
        n = len(idx_list)
    else:
        idx_list = odd_list
        divider += 1
        reminder = q
        n = len(idx_list)

    return helper(idx_list, reminder, divider, n)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        reminder = helper(list(range(1, n)), 0, 0, n-1)
        print(f"! {reminder}")

