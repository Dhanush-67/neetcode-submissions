class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        hashmap = {}

        for x in range(numCourses):
            hashmap[x] = []

        for crs, prereq in prerequisites:
            hashmap[prereq].append(crs)

        cycle, visited = set(), set()
        res = []

        def dfs(crs):
            if crs in visited:
                return True 
            if crs in cycle:
                return False

            cycle.add(crs)

            for next_crs in hashmap[crs]:
                if not dfs(next_crs):
                    return False

            visited.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
               return []
        res.reverse()
        return res