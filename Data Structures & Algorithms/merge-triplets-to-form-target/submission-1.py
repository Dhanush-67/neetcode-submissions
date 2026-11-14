class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        i,j,k = False, False, False

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if triplet[0] == target[0]:
                i = True
            if triplet[1] == target[1]:
                j = True
            if triplet[2] == target[2]:
                k = True

            if i and j and k:
                return True

        return False
        