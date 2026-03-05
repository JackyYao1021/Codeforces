from collections import defaultdict
def solve(prices):
    ans = 0
    counter = defaultdict(int)
    for price in prices:
        ans += price - (price % 10)
        counter[price % 10] += 1
    
    for j in range(0, 5):
        for i in range(9, 5, -1):
            if counter[i] > 0 and counter[10-i+j] > 0:
                tmp = min(counter[i], counter[10-i+j])
                counter[i] -= tmp
                counter[10-i+j] -= tmp
    
    for i in range(6, 10):
        if counter[i] > 0:
            ans += i * counter[i]
        
    return ans / 100.00

if __name__ == "__main__":
    n = int(input())

    prices = list(map(lambda x: int(round(x * 100)), map(float, input().split())))
    print(f"{solve(prices):.2f}")
    