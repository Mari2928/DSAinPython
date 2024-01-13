class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        Input: num1 = "123", num2 = "456"
        Output: "56088"
        """
        result = 0
        for i, digit1 in enumerate(num1[::-1]):
            tempNum1 = int(digit1) * (10 ** i)
            for j, digit2 in enumerate(num2[::-1]):
                tempNum2 = int(digit2) * (10 ** j)
                result += tempNum1 * tempNum2

        return str(result)
        
