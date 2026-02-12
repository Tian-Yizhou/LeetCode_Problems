'''
Author: Hannah
Date: 2026-01-26 10:47:07
LastEditTime: 2026-01-26 21:44:31
'''
#
# @lc app=leetcode id=1964 lang=python3
#
# [1964] Find the Longest Valid Obstacle Course at Each Position
#

# @lc code=start
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        # Method 2
        n = len(obstacles)
        ans = [0] * n

        # tails[i]: the last number with least value among all subsequences
        tails = []
        
        for i, num in enumerate(obstacles):
            # use bisect_right to find the first number that > num
            idx = bisect_right(tails, num)
            
            if idx == len(tails):
                # if num >= all numbers in tails, append it to the end
                tails.append(num)
            else:
                # otherwise, substitute the number with num
                tails[idx] = num
            ans[i] = idx + 1
                
        # the length of tails is the length of longest subsequence
        return ans
        
        # Method 1
        # This method works but will cause Time Limit Exceeded

        # ans = []
        # n = len(obstacles)
        # dp = [0] * n

        # for i in range(n):
        #     for j in range(i):
        #         if obstacles[j] <= obstacles[i]:
        #             dp[i] = max(dp[i], dp[j])
        #     dp[i] += 1
        #     ans.append(dp[i])

        # return ans
# @lc code=end

