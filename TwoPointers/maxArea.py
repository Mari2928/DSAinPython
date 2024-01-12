class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        """
        area = 0
        start = 0
        end = len(height) - 1

        while start < end:
            area = max(area, min(height[start], height[end]) * (end - start))        
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return area
            
            
        
