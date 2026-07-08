MOD = 10 ** 9 + 7
pow10 = [1] * 100001
for i in range(1, 100001):
    pow10[i] = pow10[i - 1] * 10 % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        sum = [0] * (n + 1)
        x = [0] * (n + 1)
        count = [0] * (n + 1)
        for i, c in enumerate(s):
            d = int(c)
            sum[i + 1] = sum[i] + d
            x[i + 1] = (x[i] * 10 + d) % MOD if d > 0 else x[i]
            count[i + 1] = count[i] + (d > 0)

        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            length = count[r + 1] - count[l]
            ans[i] = (x[r + 1] - x[l] * pow10[length]) * (sum[r + 1] - sum[l]) % MOD

        return ans
        # preprocessing:
        # time: O(maximum possible string length)
        # space: O(maximum possible string length)
        # n = the length of the input string
        # m = the number of queries
        # time: O(n + m)
        # space: O(n)
# from bisect import bisect_left, bisect_right
# from typing import List

# class Solution:
#     def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
#         MOD = 10**9 + 7

#         pos = []
#         dig = []

#         for i, ch in enumerate(s):
#             if ch != '0':
#                 pos.append(i)
#                 dig.append(int(ch))

#         m = len(dig)

#         # prefix digit sums
#         ps = [0] * (m + 1)
#         for i in range(m):
#             ps[i + 1] = ps[i] + dig[i]

#         # powers of 10
#         p10 = [1] * (m + 1)
#         for i in range(1, m + 1):
#             p10[i] = (p10[i - 1] * 10) % MOD

#         # prefix concatenation hash
#         pref = [0] * (m + 1)
#         for i in range(m):
#             pref[i + 1] = (pref[i] * 10 + dig[i]) % MOD

#         ans = []

#         for l, r in queries:
#             L = bisect_left(pos, l)
#             R = bisect_right(pos, r)

#             if L == R:
#                 ans.append(0)
#                 continue

#             length = R - L
#             x = (pref[R] - pref[L] * p10[length]) % MOD
#             sm = ps[R] - ps[L]

#             ans.append((x * sm) % MOD)

#         return ans