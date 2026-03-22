'''
Author: Hannah
Date: 2026-03-21 18:15:23
LastEditTime: 2026-03-21 22:40:00
'''
#
# @lc app=leetcode id=1696 lang=python3
#
# [1696] Jump Game VI
#

# @lc code=start
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # if we achieve nums[i] and get the max score, 
        # then the method must be choosing a point between
        # nums[i-k] to nums[i-1] that has max score

        n = len(nums)

        # Method 2: Monotonic queue
        score = [nums[0]] * n
        # queue containing a decreasing sequence (max scores)
        # given nums[i], choose the max in feasible window
        # then we get the max score to achieve nums[i]
        q = deque([0])
        
        for i in range(1, n):
            # eliminate unfeasible points
            while q[0] < i-k:
                q.popleft()
            
            # q[0] is the max score in feasible window, update ans
            max_s = score[q[0]] + nums[i]
            score[i] = max_s

            # add max score achieving nums[i] into q
            # maintain q decending
            while q and max_s >= score[q[-1]]:
                q.pop()
            q.append(i)
        
        return score[n-1]

            

        # Method 1: DP
        # dp[i]: the max score when achieving nums[i]
        dp = [nums[0]] * n
        for i in range(1, n):
            left = i - k if (i-k) >= 0 else 0
            dp[i] = max(dp[left:i]) + nums[i]
        
        return dp[n-1]

# @lc code=end

