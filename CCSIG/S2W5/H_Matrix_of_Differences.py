def solve(n):
    left = 1
    right = n * n
    current_left = True
    for i in range(n):
        row = []
        if i % 2 == 0:
            for j in range(n):
                if current_left:
                    row.append(left)
                    left += 1
                    current_left = False
                else:
                    row.append(right)
                    right -= 1
                    current_left = True
        else:
            for j in range(n):
                if current_left:
                    row.append(left)
                    left += 1
                    current_left = False
                else:
                    row.append(right)
                    right -= 1
                    current_left = True
            row.reverse()
        print(*row)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)