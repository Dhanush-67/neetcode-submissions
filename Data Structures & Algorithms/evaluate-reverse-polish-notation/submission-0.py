class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        length = len(tokens)
        i = 0
        lst = []
        ops = {"+","*","-","/"}

        if length == 0:
            return 0
        if length == 1:
            return int(tokens[0])

        while i < length:
            while not(tokens[i] in ops):
                lst.append(int(tokens[i]))
                i += 1
            num2 = lst.pop()
            num1 = lst.pop()

            if tokens[i] == "+":
                lst.append(num1+num2)
            elif tokens[i] == "-":
                lst.append(num1-num2)
            elif tokens[i] == "*":
                lst.append(num1*num2)
            else:
                lst.append(int(num1/num2))
            
            i += 1
        return lst[-1]
        