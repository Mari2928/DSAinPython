class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]

        Input: s = "25525511135"
        Output: ["255.255.11.135","255.255.111.35"]

        Input: s = "0000"
        Output: ["0.0.0.0"]
        """
        result = []

        def backtrack(s, address):
            if len(address) == 4:
                if s:
                    return 
                else:
                    result.append('.'.join(address))
                    return

            for i in range(1, 4):
                if i > len(s) or (s[:i][0] == '0' and len(s[:i]) > 1) or int(s[:i]) > 255:
                    return

                # create combination starting with 1 digit -> 3 digits '255' 
                address.append(s[:i]) # ['2', '5', '5', '2']
                backtrack(s[i:], address) # '5525511135' -> '525511135'->'25511135'
                address.pop()         # ['2', '5', '5']
        backtrack(s, [])
        return result
        
