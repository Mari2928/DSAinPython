class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        Input: num = 58
        Output: "LVIII"
        """
        INT_ROMAN = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 
                         40:'XL', 50:'L', 90:'XC', 100:'C', 
                         400:'CD', 500:'D', 900:'CM', 1000:'M'}
        time = 1
        result = ""
        while num:
            digit = num % 10 # 8 -> 5
            num = num // 10  # 5 -> 0
            if digit * time in INT_ROMAN:
                result = INT_ROMAN[digit * time] + result # LVIII
            elif digit > 5:
                for _ in range(digit - 5):
                    result = INT_ROMAN[1 * time] + result # III
                result = INT_ROMAN[5 * time] + result # VIII
            elif digit < 5:
                for _ in range(digit):
                    result = INT_ROMAN[1 * time] + result
            else:
                return -1
            time *= 10 # 10
        return result
