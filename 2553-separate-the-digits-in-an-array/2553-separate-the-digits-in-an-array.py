class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # nums=list(map(int,nums))
        return [int(d) for num in nums for d in str(num)]