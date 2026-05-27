class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # https://leetcode.com/problems/gas-station/solutions/1706142/javacpython-an-explanation-that-ever-exi-ctwl
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start