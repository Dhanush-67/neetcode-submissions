class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        #find first point of intersection using fast and slow pointer
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        #find start of cycle by running a slow pointer from first point of intersection
        # and the first node in the linked list

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
        