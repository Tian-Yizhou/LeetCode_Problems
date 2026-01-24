'''
Author: Hannah
Date: 2026-01-24 00:46:18
LastEditTime: 2026-01-24 01:13:35
'''
#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Method 1
        n = len(nums)
        count_map = Counter(nums)
        
        dup, missing = -1, -1
        for i in range(1, n + 1):
            if count_map[i] == 2:
                dup = i
            elif count_map[i] == 0:
                missing = i
                
            if dup != -1 and missing != -1:
                break
                
        return [dup, missing]
        
# @lc code=end

