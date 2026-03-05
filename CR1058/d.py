def query(indices):
    if not indices:
        return 0
    print(f"? {len(indices)} {' '.join(map(str, indices))}", flush=True)
    mad = int(input())
    return mad

def solve():
    n = int(input())    
    unpaired_indices = []
    ans = [-1] * (2 * n + 1)
    visited = [False] * (n + 1)
    visited[0] = True

    for i in range(1, 2 * n):
        if ans[i] != -1:
            continue
        if len(unpaired_indices) == 0:
            unpaired_indices.append(i)
            continue
            
        current_query_indices = unpaired_indices + [i]
        mad = query(current_query_indices)
        
        if mad == 0:
            unpaired_indices.append(i)
        else:
            low, high = 0, len(unpaired_indices) - 1
            partner_pos = -1
            
            while low <= high:
                if low == high:
                    partner_pos = low
                    break
                mid = (low + high) // 2
                sub_query_indices = unpaired_indices[low:mid+1] + [i]
                
                if query(sub_query_indices) == mad:
                    partner_pos = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            partner_idx = unpaired_indices[partner_pos]
            ans[i] = mad
            ans[partner_idx] = mad
            
            visited[mad] = True
            unpaired_indices.pop(partner_pos)
        
    next_value = visited.index(False)
    ans[-1] = next_value
    ans[unpaired_indices[0]] = next_value

    print("! " + " ".join(map(str, ans[1:])), flush=True)
    return 0

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()