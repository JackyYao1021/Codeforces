import heapq

def list_to_bitmask(int_list):
    mask = 0
    for i, bit in enumerate(int_list):
        if bit == 1:
            mask |= (1 << i)
    return mask

def solve(n, m, symptoms_list, medicines):
    start_mask = list_to_bitmask(symptoms_list)
    target_mask = 0

    processed_medicines = []
    for i in range(m):
        cost, remove_list, side_effect_list = medicines[i]
        remove_mask = list_to_bitmask(remove_list)
        side_effect_mask = list_to_bitmask(side_effect_list)
        processed_medicines.append((cost, remove_mask, side_effect_mask))

    num_states = 1 << n
    min_days = [float('inf')] * num_states
    
    pq = []

    min_days[start_mask] = 0
    heapq.heappush(pq, (0, start_mask))

    while pq:
        current_cost, current_state = heapq.heappop(pq)

        if current_state == target_mask:
            return current_cost

        if current_cost > min_days[current_state]:
            continue

        for cost, remove_mask, side_effect_mask in processed_medicines:
            state_after_remove = current_state & (~remove_mask)
            next_state = state_after_remove | side_effect_mask
            new_cost = current_cost + cost

            if new_cost < min_days[next_state]:
                min_days[next_state] = new_cost
                heapq.heappush(pq, (new_cost, next_state))

    return -1


def string2int_list(s):
    return [int(char) for char in s]    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        
        n, m = map(int, input().split())
        
        symptoms = string2int_list(input()) 
        
        medicines = {}
        for i in range(m):
            cost = int(input())
            remove = string2int_list(input()) 
            side_effect = string2int_list(input())
            medicines[i] = (cost, remove, side_effect)
            
        print(solve(n, m, symptoms, medicines))