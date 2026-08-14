class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur = 0
        final = 0
        total = 0

        i = 0
        j = 0

        while i < len(gas) and j < len(gas):
            final = i
            cur = cur + gas[j] - cost[j]
            if cur < 0:
                i = j+1
                j = i
                cur = 0
            else:
                j += 1

        for i in range(len(gas)):
            total += gas[i] - cost[i]

        if total < 0:
            return -1
        else:
            return final
        