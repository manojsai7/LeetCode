class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n=len(nums)
        maxlen=0
        for i in range(n):
            if n-i<=maxlen:
                break
            odd_set=set()
            even_set=set()
            for j in range(i,n):
                if nums[j]%2==0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])
                if len(odd_set)==len(even_set):
                    maxlen=max(maxlen,j-i+1)
        return maxlen
