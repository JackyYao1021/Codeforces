from collections import Counter
def solve(n, s_a, s_b):
    count_a = Counter(s_a)
    count_b = Counter(s_b)

    for char in count_b:
        if count_b[char] != count_a[char]:
            return "No"
    return "Yes"
    
    



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s_a, s_b = input().split()
        print(solve(n, s_a, s_b))