class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        index = len(digits)-1

        while index >= 0 and carry:
            if digits[index] == 9:
                digits[index] = 0
                carry = 1
            else:
                digits[index] += 1
                carry = 0
            index -= 1

        if carry:
            return [1]+digits
        return digits
        