class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        tickets.sort()

        for start,end in tickets:
            heapq.heappush(edges[start],end)

        res = []

        def dfs(current):
            while(edges[current]):
                node = heapq.heappop(edges[current])
                dfs(node)
            res.append(current)
            

        dfs("JFK")
        return res[::-1]

        