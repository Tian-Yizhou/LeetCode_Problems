#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [-1] * n
        ms = []

        # assume we copy nums and link two arrays together
        # to simulate circle
        for i in range(n*2):
            x = nums[i%n]
            while ms and x > nums[ms[-1]]:
                idx = ms.pop()
                ans[idx] = x
            # we only need to record each number once
            if i < n:
                ms.append(i)
        
        return ans

# @lc code=end

