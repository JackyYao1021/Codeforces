def solve(n, X, arr):
    arr.sort()
    left, right = 0, n - 1
    ans = 0
    ans_list = []
    remaining = 0
    while left <= right:
        temp_sum = remaining + arr[right]
        if temp_sum < X:
            remaining += arr[left]
            ans_list.append(arr[left])
            left += 1
        else:
            ans += arr[right]
            remaining = temp_sum - X
            ans_list.append(arr[right])
            right -= 1
    return ans, ans_list
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, X = map(int, input().split())
        arr = list(map(int, input().split()))
        ans, ans_list = solve(n, X, arr)
        print(ans)
        print(*ans_list)
        