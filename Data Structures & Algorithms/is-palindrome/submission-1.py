class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        lst = []

        for letter in s:
            if(letter.isalnum()):
                if letter.isupper():
                    lst.append(letter.lower())
                else:
                    lst.append(letter)

        lst_reverse = lst[::-1]

        return lst == lst_reverse