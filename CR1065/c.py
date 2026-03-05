from collections import Counter
def solve(n, a_list, b_list):
    
    A = a_list[0]
    M = b_list[0]
    
    change_list = ["S"]
    
    if a_list[0] != b_list[0]:
        change_list.append("A")
        
    
    for i in range(1, n):
        A ^= a_list[i]
        M ^= b_list[i]
        if a_list[i] != b_list[i]:
            if i % 2 == 0 and change_list[-1] != A:
                change_list.append("A")
            elif i % 2 == 1 and change_list[-1] != M:
                change_list.append("M")
    
    
    if A == M:
        return "Tie"
    else:
        counter = Counter(change_list)
        if counter["M"] > counter["A"]:
            return "Mai" 
        elif counter["M"] < counter["A"]:
            return "Ajisai"
        elif change_list[-1] == "A":
            return "Ajisai"
        elif change_list[-1] == "M":
            return "Mai"
        else:
            return "Tie"
        
            
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
        print(solve(n, a_list, b_list))