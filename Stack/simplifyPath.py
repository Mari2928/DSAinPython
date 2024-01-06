class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str

        Input: path = "/../"
        Output: "/"
        """
        dirs = path.split('/')
        stack = []
        for dir in dirs:
            if dir =='.' or not dir: continue
            elif dir == '..': 
                if stack:   stack.pop()
            else: stack.append(dir)
        return '/'+'/'.join(stack)
        
