class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.timemap.get(key)
        if not entries:
            return ""

        res = ""
        l, r = 0, len(entries) - 1
        while l <= r:
            mid = (l + r) // 2
            if entries[mid][0] <= timestamp:
                res = entries[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res