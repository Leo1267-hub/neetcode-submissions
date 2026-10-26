class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i:[] for i in range(1,n+1)}


        def dfs(v1,v2,visited):
            if v1 == v2:
                return True
            visited.add(v1)
            for nei in adj[v1]:
                if nei not in visited:
                    if dfs(nei,v2,visited):
                        return True
            return False

        for v1,v2 in edges:
            if dfs(v1,v2,set()):
                return [v1,v2]
            adj[v1].append(v2)
            adj[v2].append(v1)
