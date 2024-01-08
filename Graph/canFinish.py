class Solution:
    def canFinish(self, numCourses,  prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        
        for c, pre in prerequisites:
            graph[c].append(pre)
            
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False            
        return True
    
    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
       # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True
