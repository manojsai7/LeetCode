class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p=[0]
        for i in nums:
            p.append(p[-1]+i)
        p.pop(0)
        return p
        