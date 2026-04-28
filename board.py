from random import randint
 
RANDOM = randint(1, 10 ** 9)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM
    
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, nums)

    def build(self, node, l, r, nums):
        if l == r:
            self.tree[node] = nums[l]
            return
        mid = (l + r) // 2
        self.build(node * 2, l, mid, nums)
        self.build(node * 2 + 1, mid + 1, r, nums)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self._update(node * 2, l, mid, idx, val)
        else:
            self._update(node * 2 + 1, mid + 1, r, idx, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)

    def _query(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        ans = 0
        if ql <= mid:
            ans += self._query(node * 2, l, mid, ql, qr)
        if qr > mid:
            ans += self._query(node * 2 + 1, mid + 1, r, ql, qr)
        return ans

    def query(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)