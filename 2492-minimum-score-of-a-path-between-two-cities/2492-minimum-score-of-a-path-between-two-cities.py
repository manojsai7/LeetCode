from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # 1. Build an adjacency list for the graph
        graph = defaultdict(list)
        for u, v, distance in roads:
            graph[u].append((v, distance))
            graph[v].append((u, distance))
            
        # 2. Initialize BFS from city 1
        visited = set()
        visited.add(1)
        queue = deque([1])
        
        # Track the absolute minimum score encountered
        min_score = float('inf')
        
        # 3. Traverse the connected component
        while queue:
            current_city = queue.popleft()
            
            for neighbor, distance in graph[current_city]:
                # Update the minimum score regardless of whether the neighbor has been visited
                # because we need to check every single edge in this component
                if distance < min_score:
                    min_score = distance
                    
                # If we haven't visited the neighbor, add it to the queue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score