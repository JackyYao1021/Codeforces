from collections import deque
def solve(n, row1, row2):
    all_numbers = set()
    for a in row1:
        all_numbers.add(a)
    for b in row2:
        all_numbers.add(b)
    mx = max(all_numbers)
    mn = min(all_numbers)
    ans = (mn-1) * (2*n - mx)
    
    dq = deque(sorted(all_numbers))
    prev_l = mn
    prev_r = mx
    found_l_bound = False
    found_r_bound = False
    while len(dq) >= 2:
        l = dq.popleft()
        r = dq.pop()
        if found_l_bound and found_r_bound:
            break
        if not found_l_bound and not found_r_bound and not calculate_area(row1, row2, l, r, n):
            ans += (l-1) * (2*n - r)
            continue
        if not found_r_bound and not calculate_area(row1, row2, prev_l, r, n):
            ans += (prev_r - r) * (prev_l-1)
            tmp_r = r
        else:
            tmp_r = prev_r
            found_r_bound = True
        if not found_l_bound and calculate_area(row1, row2, l, prev_r, n):
            ans += (l - prev_l) * (2*n - tmp_r)
        else:
            tmp_l = prev_l
            found_l_bound = True
        
        prev_l = tmp_l
        prev_r = tmp_r
    return ans
    
    
    
    
def calculate_area(row1, row2, l, r, n):
    segments1 = helper(l, r, list(row1))
    segments2 = helper(l, r, list(row2))
    
    merged = union_segments(segments1, segments2)
    if len(merged) == 1 and merged[0][0] == 1 and merged[0][-1] == n:
        return True    
    return False

def union_segments(segments1, segments2):
    points = []
    for seg in segments1:
        points.append((seg[0], 'L'))
        points.append((seg[-1], 'R'))
    for seg in segments2:
        points.append((seg[0], 'L'))
        points.append((seg[-1], 'R'))
    points.sort()
    count = 0
    merged = []
    current_segment = []
    for point, typ in points:
        if typ == 'L':
            count += 1
            current_segment.append(point)
        else:
            count -= 1
            current_segment.append(point)
        if count == 0 and current_segment:
            merged.append(current_segment)
            current_segment = []
    return merged
            

def helper(l, r, row):
    ans = []
    tmp = []
    for i, val in enumerate(row):
        if l <= val <= r:
            tmp.append(i)
        else:
            if tmp:
                ans.append(tmp)
                tmp = []
    if tmp:
        ans.append(tmp)
    return ans

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        row1 = list(map(int, input().split()))
        row2 = list(map(int, input().split()))
        print(solve(n, row1, row2))