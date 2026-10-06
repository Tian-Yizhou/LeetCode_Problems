'''
Author: Hannah
Date: 2026-10-06 09:51:57
LastEditTime: 2026-10-06 10:31:45
'''
#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # NlogN time
        nums.sort()

        # Method 2: Sliding window
        # time complexity: O(nlogn + n)
        # space complexity: O(1)
        # given a window [left, right], where nums[right] = target
        # if all elements in this window can be increased to target
        # it means k >= (right-left+1) * target - sum(nums[left:right+1])
        # when k < RHS, move left to make the window valid
        left = 0
        s = 0
        ans = 0
        for right, target in enumerate(nums):
            s += nums[right]
            # if k < RHS, move left
            while k < (right-left+1) * target - s:
                s -= nums[left]
                left += 1
            # when the window is valid, update answer
            ans = max(right-left+1, ans)

        return ans         


        # Method 1: Simulation, time limit exceeded
        # time complexity: O(n^2)
        # space complexity: O(1)
        # for i-th element, the frequency is at most i+1
        ans = 0
        n = len(nums)
        for i in range(n-1, -1, -1):
            if ans >= i+1:
                break
            target = nums[i]
            k_left = k
            freq_cnt = 1
            for j in range(i-1, -1, -1):
                diff = target - nums[j]
                if k_left - diff >= 0:
                    k_left -= diff
                    freq_cnt += 1
                else:
                    break
            # update answer
            ans = max(freq_cnt, ans)

        return ans
# @lc code=end

