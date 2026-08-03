class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        s1, s2, s3 = 0, 0, 0
        tot = 0

        for value in reversed(stoneValue):
            tot += value
            s1, s2, s3 = tot-min(s1,s2,s3),s1,s2
        bob = tot - s1
        if s1 > bob:
            return "Alice"
        if s1 < bob:
            return "Bob"
        if s1 == bob:
            return "Tie"
        
"""
from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue):

        n = len(stoneValue)

        @cache
        def dfs(i):

            if i == n:
                return 0

            best = float("-inf")
            take = 0

            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                best = max(best, take - dfs(j + 1))

            return best

        diff = dfs(0)

        if diff > 0:
            return "Alice"

        elif diff < 0:
            return "Bob"

        return "Tie"
"""