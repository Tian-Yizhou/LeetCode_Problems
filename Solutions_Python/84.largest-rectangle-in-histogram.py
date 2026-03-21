'''
Author: Hannah
Date: 2026-03-20 21:47:08
LastEditTime: 2026-03-20 22:43:04
'''
#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans = 0

        # Method 2: use a gard
        # use a stack containing the idx
        # maintain a strictly increasing height sequence
        # add -1 on the right of array, this will clean elements in stack
        heights.append(-1)
        # this is the left bound for the first bar
        stack_idx = [-1]
        for right, h in enumerate(heights):
            # if current height <= the height of stack top
            # then we find the right bound of stack top
            while len(stack_idx) > 1 and h <= heights[stack_idx[-1]]:
                # the idx of stack top
                idx = stack_idx.pop()
                # the left bound of stack top is its previous bar
                left = stack_idx[-1]
                # calculate width
                w = right - left - 1
                # update ans
                ans = max(ans, heights[idx] * w)
            # add idx of current bar into stack
            stack_idx.append(right)

        return ans

        # Method 1
        # Use a stack containing the idx of rectangles whose
        # area are not decided
        stack_idx = []

        n = len(heights)

        for i in range(n):
            while stack_idx and heights[i] < heights[stack_idx[-1]]:
                height = heights[stack_idx.pop()]

                while stack_idx and height == heights[stack_idx[-1]]:
                    stack_idx.pop()
            
                if stack_idx:
                    width = i - stack_idx[-1] - 1
                else:
                    width = i
                ans = max(ans, width * height)
            # add the idx of current bar into stack
            stack_idx.append(i)

        # for those bar remianed
        while stack_idx:
            height = heights[stack_idx.pop()]
            # skip the bars with the same height
            while stack_idx and height == heights[stack_idx[-1]]:
                stack_idx.pop()
            if stack_idx:
                width = n - stack_idx[-1] - 1
            else:
                width = n
            ans = max(ans, width*height)
        
        return ans
            
# @lc code=end

