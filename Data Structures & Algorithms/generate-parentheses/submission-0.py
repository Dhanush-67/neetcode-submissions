class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(open, close):
            if close == n:
                s = ""
                for x in stack:
                    s += x
                res.append(s)

            if open < n:
                stack.append("(")
                dfs(open+1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                dfs(open, close+1)
                stack.pop()

        dfs(0,0)
        return res


        