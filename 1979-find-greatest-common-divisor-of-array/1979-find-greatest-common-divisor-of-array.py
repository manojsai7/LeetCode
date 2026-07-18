class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        minn=min(nums)
        maxx=max(nums)
        return gcd(minn,maxx)
