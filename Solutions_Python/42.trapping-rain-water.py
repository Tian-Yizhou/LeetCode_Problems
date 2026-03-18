'''
Author: Hannah
Date: 2026-03-17 23:11:50
LastEditTime: 2026-03-17 23:51:02
'''
#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        ans = 0

        # Method 3: Monotonic Stack
        # record index, maintain a decreasing height sequence
        ms = []
        for i, h in enumerate(height):
            while ms and h >= height[ms[-1]]:
                bottom = height[ms.pop()]
                # if stack becomes empty
                if not ms:
                    break
                else:
                    left = ms[-1]
                    left_height = height[left]
                    ans += (min(left_height, h) - bottom) * (i - left - 1)
            ms.append(i)
        
        return ans


        # Method 2: Two pointers
        # Space Complexity: O(1)
        pre_max, suf_max = 0, 0
        left, right = 0, n-1
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        
        return ans


        # Method 1
        # Space Complexity: O(n)
        pre_max = [0] * n
        suf_max = [0] * n
        pre_max[0], suf_max[-1] = height[0], height[-1]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])
        
        for i in range(n):
            ans += min(suf_max[i], pre_max[i]) - height[i]
        
        return ans

# @lc code=end

