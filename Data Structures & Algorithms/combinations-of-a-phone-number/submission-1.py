class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        res = []
        len_ = len(digits)
        mappy  = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z'],
        }

        lst = list(digits)

        def dfs(word, index):
            if index >= len_:
                res.append(word)
                return

            for l in mappy[digits[index]]:
                dfs(word+l,index+1)

        dfs("",0)
        return res



        
        