class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        answers = []
        for i in range(length-1):
            count = 1
            j = i+1
            flag = 0
            while temperatures[i] >= temperatures[j]:
                if j == length - 1:
                    answers.append(0)
                    flag = 1
                    break
                j += 1
                count += 1
            if flag == 0:
                answers.append(count)
        answers.append(0)
        return answers