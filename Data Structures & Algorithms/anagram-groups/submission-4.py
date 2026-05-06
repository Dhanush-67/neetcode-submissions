class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dice = defaultdict(list)
        for s in strs:
            word = tuple(sorted(s))
            dice[word].append(s)
        return list(dice.values())
        
