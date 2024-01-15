class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        Input: s = "applepenapple", wordDict = ["apple","pen"]
        Output: true

        Input: s = "abce", wordDict = ["bc","ae"]
        Output: false
        """
        Q = [s]
        seen = set()
        while Q:
            s = Q.pop(0) # leetcode -> code
            for word in wordDict: # leet -> code
                if s.startswith(word):
                    new_s = s[len(word):] # code -> ""
                    if new_s == "":
                        return True
                    if new_s not in seen: 
                        Q.append(new_s)   # [code]
                        seen.add(new_s)   # [code]
        return False
