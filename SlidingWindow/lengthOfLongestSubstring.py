class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        Input: s = "abcabcbb"
        Output: 3
        """
        max_len = 0
        start = 0
        seen = {}

        for i, char in enumerate(s):
            if char in seen and start <= seen[char]:
                start = seen[char] + 1
            else:
                crr_len = i - start + 1
                if crr_len > max_len:
                    max_len = crr_len
            seen[char] = i
        return max_len 
        
