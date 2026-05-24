def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    diff = [arr[i+1] - arr[i] for i in range(n-1)]
    mx = float("inf")
    mn = 0
    processed_diff = []
    tmp = -1
    for i in range(n-1):
        if diff[i] < 0:
            if tmp != -1:
                processed_diff.append(tmp)
                tmp = -1
            processed_diff.append(diff[i])
        else:
            tmp = max(tmp, diff[i])
    processed_diff.append(float("inf"))
    # print(processed_diff)
    for i in range(len(processed_diff)-1):
        if processed_diff[i] < 0 and processed_diff[i+1] < 0:
            print("NO")
            return
        elif processed_diff[i] > 0 and processed_diff[i+1] > 0:
            continue
        elif processed_diff[i] < 0 and processed_diff[i+1] > 0:
            mn = max(mn, -processed_diff[i])
            mx = min(mx, processed_diff[i+1])
        elif processed_diff[i] > 0 and processed_diff[i+1] < 0:
            mn = max(mn, -processed_diff[i+1])
            mx = min(mx, processed_diff[i])
    if mn <= mx:
        print("YES")
    else:
        print("NO")
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()