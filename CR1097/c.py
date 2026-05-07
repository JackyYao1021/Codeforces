def solve(n, arr, brr):
    stackA_cnt = 0
    stackB_cnt = 0
    # print(arr, brr)
    for i in range(n):
        # print(arr[i], brr[i])
        # print(stackA_cnt, stackB_cnt)
        if arr[i] == brr[i] == "(":
            stackA_cnt += 1
            stackB_cnt += 1
        elif arr[i] == brr[i] == ")":
            if stackA_cnt == 0 or stackB_cnt == 0:
                print("NO")
                return
            stackA_cnt -= 1
            stackB_cnt -= 1
        else:
            if stackA_cnt == 0 and stackB_cnt == 0:
                print("NO")
                return
            if stackA_cnt > stackB_cnt:
                stackA_cnt -= 1
                stackB_cnt += 1
            else:
                stackA_cnt += 1
                stackB_cnt -= 1
    if stackA_cnt == 0 and stackB_cnt == 0:
        print("YES")
    else:
        print("NO")
    return

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input()
        brr = input()
        solve(n, arr, brr)
        