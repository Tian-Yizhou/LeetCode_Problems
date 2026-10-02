'''
Author: Hannah
Date: 2026-10-01 18:12:05
LastEditTime: 2026-10-01 18:22:39
'''
#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
# import bisect
# from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.cur_snap_id = 0
        self.history = defaultdict(list)
        

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.cur_snap_id, val))
        

    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        # find the last snapshot with id <= snap_id
        j = bisect.bisect_left(self.history[index], (snap_id + 1, )) - 1
        return self.history[index][j][1] if j >= 0 else 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

