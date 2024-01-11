class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        """
        result = []

        def backtrack(comb, open, close):
            if len(comb) == n*2:
                result.append(comb)
                return

            if open < n:
                backtrack(comb + '(', open + 1, close)
            if close < n and open > close:
                backtrack(comb + ')', open, close + 1)
           
        backtrack("", 0, 0)
        return result
        
