class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)


    def add(self, val: int) -> int:
        index = 0
        flag = 0
        for i in range(len(self.nums)):
            if self.nums[i] < val:
                continue
            else:
                self.nums = self.nums[:i]+[val]+self.nums[i:]
                flag = 1
                break

        if flag == 0:
            self.nums.append(val)

        index = len(self.nums)
        count = 0
        while count != self.k:
            count+=1
            index -= 1

        return self.nums[index]


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)