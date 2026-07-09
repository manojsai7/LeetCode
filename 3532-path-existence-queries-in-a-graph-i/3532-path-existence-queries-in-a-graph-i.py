class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Step 1: Initialize the state trackers
        component_ids = [0] * n
        current_id = 0
        
        # Step 2: The O(N) linear sweep to group connected nodes
        for i in range(1, n):
            # If the gap breaks the maxDiff limit, start a new component group
            if nums[i] - nums[i-1] > maxDiff:
                current_id += 1
            component_ids[i] = current_id
            
        # Step 3: The O(Q) instant lookup for all queries
        return [component_ids[u] == component_ids[v] for u, v in queries]