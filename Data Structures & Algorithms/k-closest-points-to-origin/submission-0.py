class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        heapq.heapify(heap)

        for point in points:
            dist = math.sqrt((point[0]**2) + (point[1]**2))
            heapq.heappush(heap,[dist,point[0], point[1]])

        count = 0

        while count < k:
            thing = heapq.heappop(heap)
            result.append([thing[1],thing[2]])
            count += 1

        return result

        