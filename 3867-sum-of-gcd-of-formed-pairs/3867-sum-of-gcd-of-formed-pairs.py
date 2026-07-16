class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        prefixGcd=[]
        mx=nums[0]
        for i in range(len(nums)):
            if nums[i]>mx:
                mx=nums[i]
            prefixGcd.append(gcd(nums[i],mx))
        prefixGcd.sort()
        l,r=0,len(nums)-1
        x=0
        while l<r:
            x+=gcd(prefixGcd[l],prefixGcd[r])
            l+=1
            r-=1
        return x
            # if l==r:
            #     break
        
            
        