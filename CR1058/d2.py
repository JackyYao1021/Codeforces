
def query(indices):
    if not indices:
        return 0
    print(f"? {len(indices)} {' '.join(map(str, indices))}", flush=True)
    mad = int(input())
    return mad

def solve():
    n = int(input())
    ans = [-1] * (2 * n + 1)
    
    unpaired_indices = []

    for i in range(1, 2 * n + 1):

        current_query_indices = unpaired_indices + [i]
        
        mad = query(current_query_indices)

        if mad == 0:
            unpaired_indices.append(i)
        else:
            low, high = 0, len(unpaired_indices) - 1
            partner_pos_in_list = -1

            while low <= high:
                mid = (low + high) // 2
            
                sub_query_indices = unpaired_indices[:mid + 1] + [i]
                
                if query(sub_query_indices) == mad:
                    partner_pos_in_list = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            partner_idx = unpaired_indices[partner_pos_in_list]
            
            ans[i] = mad
            ans[partner_idx] = mad
        
            unpaired_indices.pop(partner_pos_in_list)

    print("! " + " ".join(map(str, ans[1:])), flush=True)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()