def solve(n, rk, ck, rd, cd):
 
    direction = (rk-rd // abs(rk-rd) if rk != rd else 0,
                 ck-cd // abs(ck-cd) if ck != cd else 0)
    m_diss_r = abs(rk-rd)
    m_diss_c = abs(ck-cd)
    
    k_rest_r = 0
    
    if direction[0] > 0:
        k_rest_r = n - rk
    elif direction[0] < 0:
        k_rest_r = rk
 
    k_rest_c = 0
    if direction[1] > 0:
        k_rest_c = n - ck
    elif direction[1] < 0:
        k_rest_c = ck
        
    diff = abs(m_diss_r - m_diss_c)    
    
    if m_diss_r < m_diss_c:
        f_stage = min(k_rest_r, diff)
        k_rest_r -= f_stage
        ans = m_diss_c
        if f_stage < diff:
            t = min(m_diss_c, m_diss_r) // 2
            if t < min(k_rest_r, k_rest_c):
                # ans += 
                k_rest_r -= t
                k_rest_c -= t
            else:
            
            
            
        ans = m_diss_c + max(k_rest_r, k_rest_c)
    else:
        f_stage = min(k_rest_c, diff)
        
        k_rest_c -= f_stage
        ans = m_diss_r + max(k_rest_r, k_rest_c)
 
    return ans
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, rk, ck, rd, cd = map(int, input().split())
        print(solve(n, rk, ck, rd, cd))
        