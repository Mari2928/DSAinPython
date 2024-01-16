class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int

        Input: version1 = "1.01", version2 = "1.001"
        Output: 0

        Input: version1 = "0.1", version2 = "1.1"
        Output: -1
        """
        ver1 = [int(x) for x in version1.split('.')]
        ver2 = [int(x) for x in version2.split('.')]

        while len(ver1) != len(ver2):
            if len(ver1) < len(ver2):
                ver1.append(0)
            else:
                ver2.append(0)

        for i in range(len(ver1)):
            if ver1[i] > ver2[i]:
                return 1
            if ver1[i] < ver2[i]:
                return -1
        
        return 0
