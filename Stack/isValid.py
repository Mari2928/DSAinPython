class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Input: s = "()[]{}"
        Output: true
        """
        mapping = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in ')}]':
                if not stack:   return False
                if stack.pop() != mapping[char]:   return False
            else:
                stack.append(char)
        return stack == []
