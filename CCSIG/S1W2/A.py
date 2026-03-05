def solve(word):
    if len(word) > 10:
        return word[0] + str(len(word)-2) + word[-1]
    else:
        return word

t = int(input())
for _ in range(t):
    word = input().strip()
    print(solve(word))