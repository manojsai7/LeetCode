from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        unique_costs = set()
        
        # Build the graph and track in-degrees for topological sorting
        for u, v, weight in edges:
            adj[u].append((v, weight))
            in_degree[v] += 1
            unique_costs.add(weight)
            
        sorted_costs = sorted(list(unique_costs))
        
        # Kahn's Algorithm to find the Topological Order
        q = deque([i for i in range(n) if in_degree[i] == 0])
        topo_order = []
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v, weight in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        # Helper function to check if a valid path exists with edge costs >= min_req
        def check(min_req: int) -> bool:
            dp = [float('inf')] * n
            dp[0] = 0
            
            for u in topo_order:
                if dp[u] == float('inf'):
                    continue
                    
                for v, weight in adj[u]:
                    # Ignore edges that drop below our required minimum score
                    if weight < min_req:
                        continue
                    # Ignore offline intermediate nodes (0 and n-1 are always guaranteed online)
                    if v != n - 1 and not online[v]:
                        continue
                    
                    # Relaxation step
                    if dp[u] + weight < dp[v]:
                        dp[v] = dp[u] + weight
                        
            # Check if we can reach the end node within the budget 'k'
            return dp[n - 1] <= k

        # Binary Search over the sorted unique edge costs
        ans = -1
        left, right = 0, len(sorted_costs) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if check(sorted_costs[mid]):
                ans = sorted_costs[mid]
                left = mid + 1  # Feasible, try to find a larger minimum edge cost
            else:
                right = mid - 1 # Not feasible, lower our requirement
                
        return ans