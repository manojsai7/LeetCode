class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        res=0
        while l<r:
            water=min(height[l],height[r])*(r-l)
            res=max(res,water)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res
"""
TLE approach
        # n=len(height)
        # res=0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         amount=min(height[i],height[j])*(j-i)
        #         res=max(res,amount)
        # return res
"""