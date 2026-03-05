def divisors(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    
    divs.sort()
    return divs


def solve(n, k, strips):
    strips_bits = []
    for i in range(n):
        bits = 0
        for j in range(k):
            bits |= (1 << (ord(strips[j][i]) - 97))
        strips_bits.append(bits)
    
    for d in divisors(n):
        sentence = []
        found = False
        for i in range(d):
            bits = (1 << 26) - 1
            for j in range(i, n, d):
                bits &= strips_bits[j]
            if bits == 0:
                found = False
                break
            else:
                found = True
                sentence.append(bits)
        if found:
            result = []
            for bits in sentence:
                char = chr((bits & -bits).bit_length() - 1 + 97)
                result.append(char)
            
            print(''.join(result*(n // d)))
            return
        
        
            
            
    
        
        


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        strips = []
        n, k = map(int, input().split())
        for _ in range(k):
            arr = input().strip()
            strips.append(arr)
        solve(n, k, strips) 
        