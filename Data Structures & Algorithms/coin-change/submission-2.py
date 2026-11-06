class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque()
        queue.append(amount)
        res = 0
        visited = set()

        while queue:
            for _ in range(len(queue)):
                total = queue.popleft()
                if total == 0:
                    return res
                if total in visited:
                    continue
                visited.add(total)
                for i in range(len(coins)):
                    if total-coins[i] >= 0:
                        queue.append(total-coins[i])
            res += 1
        return -1
        