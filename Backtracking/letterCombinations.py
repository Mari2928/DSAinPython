class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]

        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        """
        if not digits:
            return []

        result = []
        phone = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
                 "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        def backtrack(combination, nextDigit):
            if not nextDigit:
                result.append(combination)
                return
            
            for letter in phone[nextDigit[0]]: # "2"
                backtrack(combination + letter, nextDigit[1:]) #("a","3")

        backtrack("", digits)
        return result
        
