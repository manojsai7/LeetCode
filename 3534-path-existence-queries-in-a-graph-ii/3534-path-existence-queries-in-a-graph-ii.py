from bisect import bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        # 1. Sort the nodes by their values while keeping track of original indices
        sorted_indices = sorted(range(n), key=lambda i: nums[i])
        sorted_vals = [nums[i] for i in sorted_indices]
        
        # Map original index -> position in the sorted array
        pos = [0] * n
        for sorted_idx, orig_idx in enumerate(sorted_indices):
            pos[orig_idx] = sorted_idx
            
        # 2. For each sorted position, find the furthest index it can reach in 1 hop
        # R[i] = largest index j such that sorted_vals[j] - sorted_vals[i] <= maxDiff
        R = [0] * n
        for i in range(n):
            # Find the first element > sorted_vals[i] + maxDiff, then subtract 1
            idx = bisect_right(sorted_vals, sorted_vals[i] + maxDiff) - 1
            R[i] = idx

        # 3. Build the Binary Lifting (Sparse Table) for jumps
        # up[j][i] stores the index reached from position i after 2^j steps
        LOG = 18  # Since 2^17 = 131,072 > 10^5
        up = [[0] * n for _ in range(LOG)]
        up[0] = R
        
        for j in range(1, LOG):
            for i in range(n):
                up[j][i] = up[j-1][up[j-1][i]]
                
        # 4. Answer each query using binary lifting in O(log N)
        def query_dist(u, v):
            p1, p2 = pos[u], pos[v]
            if p1 == p2:
                return 0
            if p1 > p2:
                p1, p2 = p2, p1
                
            # If even the maximum possible jumps from p1 can't reach p2, they are disconnected
            if up[LOG - 1][p1] < p2:
                return -1
                
            steps = 0
            # Lift p1 as far as possible without reaching or passing p2
            for j in range(LOG - 1, -1, -1):
                if up[j][p1] < p2:
                    p1 = up[j][p1]
                    steps += (1 << j)
                    
            # One final step from the lifted position is guaranteed to land on or past p2
            return steps + 1

        return [query_dist(u, v) for u, v in queries]