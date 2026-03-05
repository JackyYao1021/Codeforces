from collections import Counter
def solve(n, x, arr):
    ans = 0
    counter = Counter(arr)
    heights = sorted(counter.keys())
    pre_height = heights[0]
    num_under = counter[pre_height]
    for height in heights[1:]:
        if ans + (height - pre_height) * num_under >= x:
            return (x - ans) // num_under + pre_height
        else:
            ans += (height - pre_height) * num_under
            num_under += counter[height]
            pre_height = height
    return pre_height + (x - ans) // num_under
            
        
        
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        print(solve(n, x, arr))