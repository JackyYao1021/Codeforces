def solve(n, min_values, snd_min_values):
    min_snd = min(snd_min_values)
    min_fst = min(min_values)
    
    print(sum(snd_min_values) - min_snd + min_fst)
        

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        min_values = []
        snd_min_values = []
        for i in range(n):
            m = int(input())
            arr = list(map(int, input().split()))
            arr.sort()
            min_values.append(arr[0])
            snd_min_values.append(arr[1])
        solve(n, min_values, snd_min_values)