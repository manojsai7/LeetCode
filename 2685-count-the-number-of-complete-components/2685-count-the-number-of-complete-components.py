from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            degree = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    n_nodes, n_degree = dfs(nei)
                    nodes += n_nodes
                    degree += n_degree

            return nodes, degree

        for i in range(n):
            if not visited[i]:
                nodes, degree = dfs(i)

                if degree == nodes * (nodes - 1):
                    ans += 1

        return ans