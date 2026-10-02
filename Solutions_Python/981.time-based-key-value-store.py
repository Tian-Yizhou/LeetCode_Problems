'''
Author: Hannah
Date: 2026-10-01 18:12:10
LastEditTime: 2026-10-01 18:42:12
'''
#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
# from collections import defaultdict
# import bisect
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamp of each key is increasing
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        # find the smallest index s.t. store[key][idx][0] > timestamp
        idx = bisect.bisect_right(self.store[key], timestamp, key=lambda x: x[0]) - 1
        if idx >= 0:
            return self.store[key][idx][1]
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

