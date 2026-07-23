class TimeMap:

    def __init__(self):
        self.mp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.mp.get(key)
        if key not in self.mp:
            return ""
        l = 0
        r = len(values)-1
        while l <= r:
            mid = (l+r)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid +1
            else:
                r = mid -1
        return res

        
