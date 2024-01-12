class Solution:
    def longestPalindrome(self, s):
        """
        Input: s = "babad"
        Output: "bab"
        """
        longest_palindrom = s[-1]
        dp = [[0]*len(s) for _ in range(len(s))]

        # one char is palindrome
        for i in range(len(s)):
            dp[i][i] = True
        
        # move str backwards and check forwards
        for i in range(len(s)-1, -1, -1): 
            for j in range(i + 1, len(s)):  
                if s[i] == s[j]:  
                    # it's one char, or prev char is palindrome 
                    if j - i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1] # (1, 3) babad -> aba
                
        return longest_palindrom
