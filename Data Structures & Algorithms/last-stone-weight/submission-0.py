class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            if stone1 == stone2:
                continue
            elif stone1 >= stone2:
                heapq.heappush(heap, -(stone1-stone2))
            else:
                heapq.heappush(heap, -(stone2-stone1))

        if len(heap) == 0:
            return 0
        else:
            return -heapq.heappop(heap)
        