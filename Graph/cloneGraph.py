"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    # BFS
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node

        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]
        """
        if not node: return node
        copy = {}
        visited = []
        Q = []
        Q.append(node)
        while Q:
            cur = Q.pop(0)
            if cur in visited: 
                continue
            visited.append(cur)
            if cur not in copy:
                copy[cur] = Node(cur.val)
            for adj in cur.neighbors:
                if adj not in copy:
                    copy[adj] = Node(adj.val)
                copy[cur].neighbors.append(copy[adj])
                Q.append(adj)
        return copy[node]

    # DFS
    def cloneGraph2(self, node):
        if not node: return node
        copy = {}
        visited = []
        Q = []
        self.dfs(visited, copy, node)
        return copy[node]
    
    def dfs(self, visited, copy, node):
        if node not in visited:
            visited.append(node)
            if node not in copy:
                copy[node] = Node(node.val)            
            for adj in node.neighbors:
                if adj not in copy:
                    copy[adj] = Node(adj.val)
                copy[node].neighbors.append(copy[adj])
                self.dfs(visited, copy, adj)

        
