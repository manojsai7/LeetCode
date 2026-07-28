class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        temp = 0

        for num in nums:
            if num == 1:
                temp += 1
            else:
                if temp > max:
                    max = temp
                temp = 0

        if temp > max:
            max = temp
            
        return max
                