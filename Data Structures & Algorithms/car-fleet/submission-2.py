class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)
        pair = []
        for i in range(length):
            sublist = (position[i], speed[i])
            pair.append(sublist)
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)