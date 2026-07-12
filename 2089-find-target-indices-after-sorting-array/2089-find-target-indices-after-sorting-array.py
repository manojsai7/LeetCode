class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        x=[]
        for i in range(len(nums)):
            if nums[i]==target:
                x.append(i)
        return x
        