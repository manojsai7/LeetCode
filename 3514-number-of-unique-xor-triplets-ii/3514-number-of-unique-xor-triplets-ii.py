class Solution:
    def uniqueXorTriplets(self, V: List[int]) -> int:
        X2 = {0}                                # XOR of pairs
        X3 = set(V)                             # XOR of triplets

        k = 1 << max(V).bit_length()

        while V:
            v = V.pop()                         # pop :: prevents reuse below

            X3 |= {v ^ x2 for x2 in X2}         # existing pair ^ current value => triplet
            X2 |= {v ^ vv for vv in V}          # any value ^ current value => pair
            
            if len(X3) == k: break
        
        return len(X3)
# class Solution:
#     def uniqueXorTriplets(self, nums: List[int]) -> int:
#         MAX_XOR = 2048

#         pair_xor = [False] * MAX_XOR
#         triplet_xor = [False] * MAX_XOR

#         n = len(nums)

#         for i in range(n):
#             for j in range(i, n):
#                 pair_xor[nums[i] ^ nums[j]] = True

#         for x in range(MAX_XOR):
#             if not pair_xor[x]:
#                 continue

#             for v in nums:
#                 triplet_xor[x ^ v] = True

#         return sum(triplet_xor)