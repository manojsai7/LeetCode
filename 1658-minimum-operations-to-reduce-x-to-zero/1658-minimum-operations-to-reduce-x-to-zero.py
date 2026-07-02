class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        if target<0:
            return -1
        if target==0:
            return len(nums)
        l,curr=0,0
        maxlen=-1
        for r in range(len(nums)):
            curr+=nums[r]
            while curr>target:
                curr-=nums[l]
                l+=1
            if curr==target:
                maxlen=max(maxlen,r-l+1)
        return -1 if maxlen==-1 else len(nums)-maxlen
            
        