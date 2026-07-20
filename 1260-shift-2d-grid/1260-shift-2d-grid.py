class Solution(object):
    def shiftGrid(self, grid, k):
        l, m, n, k = [num for row in grid for num in row], len(grid), len(grid[0]), k % (len(grid) * len(grid[0]))  # grid to list
        l = l[-k:] + l[:-k]  # shift k times
        return [l[i * n: i * n + n] for i in range(m)]  # list to grid
# class Solution:
#     def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
#         m = len(grid)
#         n = len(grid[0])

#         total = m * n
#         k %= total

#         ans = [[0] * n for _ in range(m)]

#         for i in range(m):
#             for j in range(n):

#                 old = i * n + j
#                 new = (old + k) % total

#                 r = new // n
#                 c = new % n

#                 ans[r][c] = grid[i][j]

#         return ans
