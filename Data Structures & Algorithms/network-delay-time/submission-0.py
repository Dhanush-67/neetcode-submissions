class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = collections.defaultdict(list)
        res = 0

        for u, v, w in times:
            adj_map[u].append((v, w))

        visit = set()
        min_heap = [(0, k)]

        while min_heap:
            w, node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)
            res = max(res, w)
            for nei, w2 in adj_map[node]:
                if nei not in visit:
                    heapq.heappush(min_heap, (w + w2, nei))

        if len(visit) == n:
            return res
        return -1