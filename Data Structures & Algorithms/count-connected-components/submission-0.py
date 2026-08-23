class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #immediately thinking DFS
        #if we find a node, we mark it, in a set
            #track parent, so we don't DFS back
            #actually optional since we have the set
        
        #for loop that runs DFS if not in set, from 0 to n-1
        #tally

        #adjacency list (in a hashmap)

        visited = set()
        adj = {}

        #set up adjaceny list, neighbors of node
        for i in range(n):
            adj[i] = []
        for x, y, in edges:
            adj[x].append(y)
            adj[y].append(x)


        def dfs(node):
            #mark as visited
            visited.add(node)

            for nei in adj[node]:
                if nei in visited:
                    continue
                dfs(nei)
    
        tally = 0
        for i in range(n):
            #dfs will mark everything its connected to
            #if not visited, it must be in a seperate component
            if i not in visited:

                dfs(i)
                tally += 1

        return tally