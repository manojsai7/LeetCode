class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total=sum(nums)
        lsum=0
        for i in range(len(nums)):
            rsum=total-lsum-nums[i]
            if rsum== lsum:
                return i
            lsum+=nums[i]
        return -1
"""
        total=sum(nums)
        left=0
        for i,num in enumerate(nums):
            if left==total-left-num:
                return i
            left+=num
        return -1       
"""