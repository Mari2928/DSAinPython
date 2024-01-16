class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        '''
        Input: s = "eceba"
        Output: 3
        Explanation: The substring is "ece" which its length is 3.
        '''
        start, res = 0, 0
        seen = collections.Counter()

        for end in range(len(s)):
            seen[s[end]] += 1
            while len(seen) > 2:
                seen[s[start]] -= 1
                if seen[s[start]] == 0:
                    del seen[s[start]]
                start += 1
            res = max(res, end - start + 1)
        
        return res
