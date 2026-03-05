def solve(n):
    binary = bin(n)[2:]
    new_binary = binary
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '0':
            new_binary = '0' + new_binary
        else:
            break
    length = len(new_binary)
    if length % 2 == 1:
        if new_binary[length//2] == '1':
            return "NO"
    for i in range(length//2):
        if new_binary[i] != new_binary[length - 1 - i]:
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))