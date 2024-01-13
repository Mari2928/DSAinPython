class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]

        Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
        Output: [[1,5],[6,9]]

        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        Output: [[1,2],[3,10],[12,16]]
        Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
        """
        result = []
        s, e = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            if intervals[i][0] > e:
                result.append([s, e])
                return result + intervals[i:]
            elif intervals[i][1] < s:
                result.append(intervals[i])
            else:
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])
        result.append([s, e])
        return result
