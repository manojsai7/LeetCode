from typing import List
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[0] * n for _ in range(m)]
        rank = [0] * (m + n)

        value_cells = defaultdict(list)
        for r in range(m):
            for c in range(n):
                value_cells[matrix[r][c]].append((r, c))

        for value in sorted(value_cells):
            dsu = DSU(m + n)

            for r, c in value_cells[value]:
                dsu.union(r, c + m)

            groups = defaultdict(list)
            for r, c in value_cells[value]:
                groups[dsu.find(r)].append((r, c))

            updates = {}
            for root, cells in groups.items():
                max_rank = 0
                for r, c in cells:
                    max_rank = max(max_rank, rank[r], rank[c + m])
                updates[root] = max_rank + 1

            for root, cells in groups.items():
                new_rank = updates[root]
                for r, c in cells:
                    ans[r][c] = new_rank
                    rank[r] = new_rank
                    rank[c + m] = new_rank

        return ans