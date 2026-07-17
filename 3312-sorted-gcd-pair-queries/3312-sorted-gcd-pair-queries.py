from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        MAX_VAL = max(nums)
        
        # Step 1: Frequency of each number
        freq = [0] * (MAX_VAL + 1)
        for num in nums:
            freq[num] += 1
        
        # Step 2: Count multiples for each d
        multiples_count = [0] * (MAX_VAL + 1)
        for d in range(1, MAX_VAL + 1):
            count = 0
            for multiple in range(d, MAX_VAL + 1, d):
                count += freq[multiple]
            multiples_count[d] = count
        
        # Step 3: Count pairs with EXACT GCD = d
        exact_gcd = [0] * (MAX_VAL + 1)
        for d in range(MAX_VAL, 0, -1):
            # Total pairs from numbers that are multiples of d
            total_pairs = (multiples_count[d] * (multiples_count[d] - 1)) // 2
            
            # Subtract pairs with GCD = 2d, 3d, 4d, ...
            for multiple in range(2 * d, MAX_VAL + 1, d):
                total_pairs -= exact_gcd[multiple]
            
            exact_gcd[d] = total_pairs
        
        # Step 4: Build prefix sum (cumulative count of pairs)
        prefix = []
        cumulative = 0
        for d in range(1, MAX_VAL + 1):
            if exact_gcd[d] > 0:
                cumulative += exact_gcd[d]
                prefix.append((cumulative, d))
        
        # Step 5: Answer queries using binary search
        total_pairs = len(nums) * (len(nums) - 1) // 2
        result = []
        
        for q in queries:
            # Find smallest d where cumulative > q
            lo, hi = 0, len(prefix) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid][0] > q:
                    hi = mid
                else:
                    lo = mid + 1
            result.append(prefix[lo][1])
        
        return result