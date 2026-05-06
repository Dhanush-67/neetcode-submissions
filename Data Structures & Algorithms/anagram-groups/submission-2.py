class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dice = {}

        for s in strs:
            word = tuple(sorted(s))
            if word not in dice:
                dice[word] = [s]
            else:
                dice[word].append(s)
        
        return list(dice.values())
