class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hashmap = {}
        for i in hand:
            hashmap[i] = 1 + hashmap.get(i, 0)

        unique = sorted(hashmap.keys())

        for i in unique:
            count = hashmap[i]
            if count > 0:
                for j in range(groupSize):
                    if hashmap.get(i + j, 0) < count:
                        return False
                    hashmap[i + j] -= count
        return True