class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slw=0
        for fst in range(len(nums)):
            if nums[fst]%2==0:

                nums[slw],nums[fst]=nums[fst],nums[slw]
                slw+=1
        return nums
        