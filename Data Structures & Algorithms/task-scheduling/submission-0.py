class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        queue = deque()
        time = 0

        for task in tasks:
            freq[task] = freq.get(task,0) + 1
            
        heap = []

        for x in freq:
            heapq.heappush(heap,(-freq[x],x))

        while True:
            if not (queue or heap):
                break
            if queue and queue[0][0] == time:
                cooldown,task = queue.popleft()
                heapq.heappush(heap,(-freq[task],task))

            if heap:
                _, task = heapq.heappop(heap)
                freq[task] -= 1
                if freq[task]:
                    queue.append([time+n+1,task])
            time += 1

        return time

        



        