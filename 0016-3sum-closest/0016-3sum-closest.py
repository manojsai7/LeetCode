class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=nums[0]+nums[1]+nums[2]
        n=len(nums)
        # r=n-1
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if abs(total-target)<abs(closest-target):
                    closest=total
                if target>total:
                    l+=1
                elif target<total:
                    r-=1
                else:
                    return total
        return closest
