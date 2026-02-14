'''
Author: Hannah
Date: 2026-02-01 11:25:16
LastEditTime: 2026-02-14 11:22:57
'''
#
# @lc app=leetcode id=2080 lang=python3
#
# [2080] Range Frequency Queries
#

# @lc code=start
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr

        positions = defaultdict(list)
        for i, x in enumerate(arr):
            positions[x].append(i)
        self.positions = positions

    
    def bisect(self, nums, target):

        # sort the nums in advance

        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def query(self, left: int, right: int, value: int) -> int:
        
        # Mehod 3: use bisect_left, bisect_right
        pos = self.positions[value]

        # bisect_left(arr, target):
        idx_start = bisect_left(pos, left)
        idx_end = bisect_right(pos, right)

        return idx_end - idx_start

        # Method 2: find the number of indices in the range [left, right+1]
        # pos = self.positions[value]

        # idx_start = self.bisect(pos, left)
        # idx_end = self.bisect(pos, right+1)
        # # same as method 1, idx_end is the first idx >= right
        # ans = idx_end - idx_start
        
        # return ans

        # Method 1: Time Limit Error
        # cut the subarr and find the range of value
        # subarr = self.arr[left: right+1]
        # subarr.sort()

        # idx_start = self.bisect(subarr, value)
        # # note here idx_end is not the end index of value
        # idx_end = self.bisect(subarr, value+1)
        # # idx_end -1 is the end index of value
        # # but the calculation requires + 1
        # ans = idx_end - idx_start

        # return ans

        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end

