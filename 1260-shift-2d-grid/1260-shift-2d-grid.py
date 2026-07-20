class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        for _ in range(k):

            last = grid[m - 1][n - 1]

            # Shift every element one position right
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):

                    if i == 0 and j == 0:
                        continue

                    if j == 0:
                        grid[i][j] = grid[i - 1][n - 1]
                    else:
                        grid[i][j] = grid[i][j - 1]

            grid[0][0] = last

        return grid