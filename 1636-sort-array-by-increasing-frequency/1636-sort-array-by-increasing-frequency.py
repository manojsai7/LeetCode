class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        out = list(map.items())
        out.sort(key=lambda x: (x[1], -x[0]))

        ans = []
        for o in out:
            for _ in range(o[1]):
                ans.append(o[0])

        return ans        
        #BUBBLE SoRT
        # f={}
        # for i in nums:
        #     f[i]=f.get(i,0)+1
        #     n=len(nums)
        # for i in range(n-1):
        #     for j in range(n-i-1):
        #         a,b=nums[j],nums[j+1]
        #         if f[a]>f[b] or (f[a]==f[b] and a<b):
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        # return nums
