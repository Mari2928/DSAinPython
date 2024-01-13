class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        Input: x = 2.00000, n = 10
        Output: 1024.00000

        Input: x = 2.00000, n = -2
        Output: 2**(-2) = (1/2)**2 = 1/4 = 0.25000
        """

        def pow(x, n):
            if n == 0:
                return 1 
            
            temp = pow(x, n / 2)
            if n % 2 == 0:
                return temp * temp
            else:
                return temp * temp * x

        if n < 0:
            return 1 / pow(x, -n)
        else:
            return pow(x, n)
