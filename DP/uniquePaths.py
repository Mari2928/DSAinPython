class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        Input: m = 3, n = 2
        Output: 3
        """
        cache = {}
        def findPath(m, n):
            if (m, n) in cache:
                return cache[(m, n)]
            if m == 1 or n == 1:
                return 1
            
            cache[(m, n)] = findPath(m - 1, n) + findPath(m, n - 1)

            return cache[(m, n)]
        
        return findPath(m, n)
