class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return r-l+1
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         l,r,maxlen,zeros=0,0,0,0
#         n=len(nums)
#         while r<n:
#             if nums[r]==0:
#                 zeros+=1
#             while zeros>k:
#                 if nums[l]==0:

#                     zeros-=1
#                 l+=1
#             # if zeros<=k:
#             maxlen=max(maxlen,r-l+1)
#             r+=1
#         return maxlen