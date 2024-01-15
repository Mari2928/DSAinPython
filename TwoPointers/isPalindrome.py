class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Input: s = "A man, a plan, a canal: Panama"
        Output: true -> "amanaplanacanalpanama"
        """
        s = [c.lower() for c in s if c.isalnum()]
        
        for i in range(len(s)//2):
            if s[i] != s[~i]: # (0, -1) -> (1, -2)
                return False
        return True
        
