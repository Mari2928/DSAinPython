class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        '''
        Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        Output: 3
        '''
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start
