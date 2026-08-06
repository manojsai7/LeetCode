class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        nums.sort()
        maxx=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>maxx:
                maxx=nums[i]-nums[i-1]
        return maxx
        