class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = []
        
        for _ in range(n):
            adj.append([])

        for x,z in edges:
            adj[x].append(z)
            adj[z].append(x)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        
        components = 0

        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components                     