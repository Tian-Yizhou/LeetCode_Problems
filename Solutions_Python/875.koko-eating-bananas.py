'''
Author: Hannah
Date: 2026-02-01 11:25:34
LastEditTime: 2026-02-14 13:22:30
'''
#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)

        # Method 2: koko cannot finish bananas when k=0; and
        # koko can finish bananas when k=max(p[i])
        left, right = 0, max(piles)

        while left+1 < right:
            mid = (left + right) // 2
            # koko can finish bananas when k=mid
            if sum((p-1)//mid for p in piles) <= h - n:
                right = mid
            # koko cannot finish bananas when k=mid
            else:
                left = mid
        
        return right


        # Method 1
        # we don't know whether koko can finish the bananas if k=1 or k=max(p[i])-1
        # left, right = 1, max(piles)

        # while left <= right:
        #     mid = (left + right) // 2
        #     if sum((p-1)//mid for p in piles) <= h - n:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # return left

# @lc code=end

