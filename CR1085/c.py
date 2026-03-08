from collections import defaultdict
from random import randint

RANDOM = randint(1, 10 ** 9)

class Wrapper(int):
    def __new__(cls, x):
        return int.__new__(cls, x)

    def __hash__(self):
        return super().__hash__() ^ RANDOM


def helper(count, diff):
    keys = sorted(count.keys())

    previous = keys[0]
    tmp_count = count[previous]
    tmp_sum = 0
    count[previous] = 0

    for key in keys[1:]:
        need = (key - previous) * tmp_count
        if tmp_sum + need < diff:
            tmp_sum += need
            tmp_count += count[key]
            count[key] = 0
            previous = key
        else:
            sub_diff = diff - tmp_sum
            real_diff = sub_diff // tmp_count
            rem = sub_diff % tmp_count

            count[previous + real_diff] += tmp_count - rem
            if rem:
                count[previous + real_diff + 1] += rem
                return previous + real_diff + 1
            return previous + real_diff

    sub_diff = diff - tmp_sum
    real_diff = sub_diff // tmp_count
    rem = sub_diff % tmp_count

    count[previous + real_diff] += tmp_count - rem
    if rem:
        count[previous + real_diff + 1] += rem
        return previous + real_diff + 1
    return previous + real_diff


def solve(n, m, l, arr):
    count = defaultdict(int)
    count[Wrapper(0)] = m

    prev = 0
    for curr in arr:
        diff = curr - prev
        mx = helper(count, diff)

        count[Wrapper(mx)] -= 1
        count[Wrapper(0)] += 1

        if count[Wrapper(mx)] == 0:
            del count[Wrapper(mx)]

        prev = curr

    last = l - prev
    mx = helper(count, last)
    print(mx)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, l = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(n, m, l, arr)