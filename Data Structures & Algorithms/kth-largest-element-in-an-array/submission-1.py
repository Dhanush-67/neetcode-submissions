class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        result = 0
        while k != 0:
            result = -heapq.heappop(heap)
            k -= 1

        return result
        