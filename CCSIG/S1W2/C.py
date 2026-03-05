n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

index = 0
cnt = 0
while index < n:
    if arr[index] < 0:
        cnt += 1
    else:
        break
    index += 1


if cnt <= k:
    ans = sum(arr[cnt:]) - sum(arr[:cnt])
    if (cnt - k) % 2 == 1:
        if cnt > 0 and cnt < n:
            ans -= min(-arr[cnt-1], arr[cnt]) * 2
        elif cnt == 0:
            ans -= arr[cnt] * 2
        elif cnt == n:
            ans -= (-arr[cnt-1]) * 2

else:
    ans = sum(arr[k:]) - sum(arr[:k])

print(ans)