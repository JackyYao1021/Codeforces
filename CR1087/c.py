import sys

def ask_query(i, j):
    print(f"? {i} {j}")
    sys.stdout.flush()
    return int(input())

def solve(n):
    res = ask_query(1, 2)
    if res == 1:
        print(f"! 1")
        sys.stdout.flush()
        return
    res = ask_query(2, 3)
    if res == 1:
        print(f"! 2")
        sys.stdout.flush()
        return
    res = ask_query(1, 3)
    if res == 1:
        print(f"! 3")
        sys.stdout.flush()
        return
    for i in range(4, 2*n, 2):
        res = ask_query(i, i+1)
        if res == 1:
            print(f"! {i}")
            sys.stdout.flush()
            return
        
    print(f"! {2*n}")



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)
        