class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m1=min(nums)
        m2=max(nums)
        x=[]
        for i in range(m1,m2):
            if i not in nums:
                x.append(i)
        return x
        

        