'''
Author: Hannah
Date: 2026-02-01 11:24:57
LastEditTime: 2026-02-13 00:32:05
'''
#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#

# @lc code=start
class Solution:
    def bisect(self, nums, target):
        n = len(nums)
        left, right = 0, n-1
        # we sort the original array potions, so we don't need to sort here
        if nums[right] < target:
            return n
        if nums[left] > target:
            return 0
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)

        ans = []

        for x in spells:
            target = int(success / x) + (1 if success % x != 0 else 0)
            # target = int((success-1)/x) + 1
            # find the idx where numbers in product[:idx] are smaller than success
            idx = self.bisect(potions, target)
            ans.append(m-idx)
        
        return ans

# @lc code=end

