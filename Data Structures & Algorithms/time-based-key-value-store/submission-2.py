class TimeMap:

    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.m:
            self.m[key].append((value, timestamp))
        else:
            self.m[key] = [(value, timestamp)]
        print(self.m)

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        if not key in self.m:
            return ""
        arr = self.m[key]
        r = len(arr) - 1

        while l <= r:
            mid = (l+r)//2
            time = arr[mid][1]
            if time == timestamp:
                return arr[mid][0]
            elif time > timestamp:
                r = mid-1
            else:
                l = mid+1
        if arr[r][1] > timestamp:
            return ""
        return arr[r][0]


        
