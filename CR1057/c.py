from collections import Counter
def solve(sides):
    counter = Counter(sides)
    ans = 0
    cnt = 0
    side_set = set()
    for k, v in counter.items():
        if v >= 2:
            ans += (v // 2) * 2 * k
            counter[k] = v % 2
            cnt += v // 2
        if counter[k] > 0:
            side_set.add(k)
    side_list = sorted(list(side_set), reverse=True)
    side_list.append(0)
    if ans == 0:
        return 0
    for i in range(len(side_list) - 1):
        if side_list[i] - side_list[i + 1] < ans:
            return ans + side_list[i] + side_list[i + 1]
    
    if cnt >= 2:
        return ans
    else:
        return 0
            
            


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        sides = list(map(int, input().split()))
        print(solve(sides))