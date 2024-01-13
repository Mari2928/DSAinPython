class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        """
        result = {}

        for string in strs:
            key = ''.join(sorted(string))
            if key in result:
                result[key].append(string)
            else:
                result[key] = [string]
            
        return list(result.values())
         
        
