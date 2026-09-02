class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
        # n = len(nums1)
        # e = 0
        # o = 0
        # for i in range(1, n):
        #     if (nums1[i] - nums1[i-1]) % 2 == 0:
        #         e += 1
        #     else:
        #         o += 1
        # return e == n-1 or o == n-1
