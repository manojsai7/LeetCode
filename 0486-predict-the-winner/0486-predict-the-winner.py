from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def dfs(left, right):

            if left == right:
                return nums[left]

            takeLeft = nums[left] - dfs(left + 1, right)
            takeRight = nums[right] - dfs(left, right - 1)

            return max(takeLeft, takeRight)

        return dfs(0, len(nums) - 1) >= 0