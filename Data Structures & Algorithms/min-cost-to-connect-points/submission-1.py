class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        parent = []

        for i in range(len(points)):
            parent.append(i)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                heapq.heappush(minHeap,[abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j])

        totalCost = 0
        count = 0

        def find(i):
            while i != parent[i]:
                i = parent[i]
            return i

        def union(i,j):
            parenti = find(i)
            parentj = find(j)

            if parenti != parentj:
                parent[parentj] = parenti
                return True
            return False


        while count < len(points)-1:
            cost,i,j = heapq.heappop(minHeap)
            if union(i,j):
                totalCost += cost
                count += 1

        return totalCost
        