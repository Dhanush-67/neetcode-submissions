class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = 0
        final = 0

        i = 0
        j = 0

        if sum(gas) < sum(cost):
            return -1

        while i < len(gas) and j < len(gas):
            final = i
            cur = cur + gas[j] - cost[j]
            if cur < 0:
                i = j+1
                j = i
                cur = 0
            else:
                j += 1
        
        return final
        