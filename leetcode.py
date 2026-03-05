class Solution:
    def minCost(self, lists):
        n = len(lists)
        lens = [len(a) for a in lists]

        vals = sorted({x for a in lists for x in a})

        N = 1 << n
        len_sum = [0] * N
        for mask in range(1, N):
            lb = mask & -mask
            i = (lb.bit_length() - 1)
            len_sum[mask] = len_sum[mask ^ lb] + lens[i]

        median_val = [0] * N
        median_val[0] = 0  # 不会用到
        for mask in range(1, N):
            L = len_sum[mask]
            k = (L - 1) // 2  # 0-index 的第 k 小

            lo, hi = 0, len(vals) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                x = vals[mid]
                cnt = 0

                m = mask
                while m:
                    lb = m & -m
                    i = lb.bit_length() - 1
                    cnt += bisect_right(lists[i], x)
                    m ^= lb

                if cnt > k:
                    hi = mid
                else:
                    lo = mid + 1

            median_val[mask] = vals[lo]

        # 子集 DP
        dp = [inf] * N
        for i in range(n):
            dp[1 << i] = 0

        for mask in range(1, N):
            if mask & (mask - 1) == 0:  # 单元素子集
                continue

            # 枚举真子集 a（避免重复：只算 a < b）
            a = (mask - 1) & mask
            while a:
                b = mask ^ a
                if a < b:
                    cost = (dp[a] + dp[b] +
                            len_sum[a] + len_sum[b] +
                            abs(median_val[a] - median_val[b]))
                    if cost < dp[mask]:
                        dp[mask] = cost
                a = (a - 1) & mask

        return dp[N - 1]

    
if __name__ == "__main__":
    from bisect import bisect_right
    from math import inf
    
    lists = [[1,3,5],[2,4],[6,7,8]]
    solution = Solution()
    print(solution.minCost(lists))