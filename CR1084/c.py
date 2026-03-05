def solve(n, s):
    idx = 0
    rest = ""
    new_rest = s
    while rest != new_rest:
        rest = new_rest
        new_rest = []
        idx = 0
        while idx < len(rest)-1:
            if rest[idx] == rest[idx+1]:
                idx += 2
            else:
                new_rest.append(rest[idx])
                idx += 1
        if idx == len(rest)-1:
            new_rest.append(rest[idx])
        new_rest = "".join(new_rest)
        
    if len(rest) % 2 == 1:
        print("NO")
        return 
    elif len(rest) == 0:
        print("YES")
        return
    else:
        for i in range(len(rest) // 2):
            if rest[i] != rest[len(rest) -1 - i]:
                print("NO")
                return
        print("YES")
    return 
        
        
        
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        solve(n, s)