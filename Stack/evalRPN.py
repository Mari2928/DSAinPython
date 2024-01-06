class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int

        Input: tokens = ["4","13","5","/","+"]
        Output: 6
        """
        stack = []
        for token in tokens:
            if token not in "+*/-":
                stack.append(int(token))
            else:
                y = stack.pop() # pop right token first
                x = stack.pop()
                if token == "+": stack.append(x + y)
                elif token == "-": stack.append(x - y) 
                elif token == "*": stack.append(x * y) 
                else: stack.append(int(float(x) / y))                 
        return stack.pop()
        
