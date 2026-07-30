class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slw=0
        for fst in range(len(nums)):
            if nums[fst]!=0:

                nums[slw],nums[fst]=nums[fst],nums[slw]
                slw +=1
        