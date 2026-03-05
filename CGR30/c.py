from bisect import bisect_left, bisect_right, insort
from heapq import heappop, heappush, heapify
def solve(n, m, damage_list, good_monster_list, bad_monster_list):
    ans = 0
    heapify(damage_list)
    removed = []
    good_monster_list.sort()
    bad_monster_list.sort()
    for value, sword in good_monster_list:
        while damage_list:
            damage = heappop(damage_list)
            if damage >= value:
                ans += 1
                damage = max(sword, damage)
                heappush(damage_list, damage)
                break
            else:
                removed.append(damage)
    
    damage_list.extend(removed)
    damage_list.sort()
    idx = 0
    for value in bad_monster_list:
        while idx < n:
            if damage_list[idx] >= value:
                ans += 1
                idx += 1
                break
            else:
                idx += 1
    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        damage_list = list(map(int, input().split()))
        value_list = list(map(int, input().split()))
        new_sword = list(map(int, input().split()))
        good_monster_list = []
        bad_monster_list = []
        for i in range(m):
            if new_sword[i] > 0:
                good_monster_list.append((value_list[i], new_sword[i]))
            else:
                bad_monster_list.append(value_list[i])
        print(solve(n, m, damage_list, good_monster_list, bad_monster_list))
        
    