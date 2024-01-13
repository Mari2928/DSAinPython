class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        Output: [0,2,1,3]
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for course, prereq in prerequisites:
            graph[course].append(prereq) 
        result = []

        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            
            visited[i] = -1

            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            result.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []            
        return result
        
