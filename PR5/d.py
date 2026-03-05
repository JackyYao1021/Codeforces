from collections import defaultdict

def solve(n, arr):
    not_pick_dict = defaultdict(lambda: [0, 0])
    pick_dict = defaultdict(lambda: [0, 0])
    dp = [0] * (n + 1)
    not_pick_dict[arr[0]] = [0, 0]
    pick_dict[arr[0]] = [0, 1]
    for i, num in enumerate(arr[1:], start=1):
        not_idx, not_val = not_pick_dict[num-1]
        p_idx, p_val = pick_dict[num-1]
        
        pick_dict[num] = [i, not_val + i - not_idx]
        not_pick_dict[num] = [i, p_val + i - p_idx - 1]
        dp[i] = max(pick_dict[num][1], not_pick_dict[num][1])
        print(f"i: {i}, num: {num}, pick: {pick_dict[num]}, not_pick: {not_pick_dict[num]}")

    return n - max(pick_dict[arr[-1]][1], not_pick_dict[arr[-1]][1])

if __name__ == "__main__":

    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(n, arr))
        


