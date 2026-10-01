'''
Author: Hannah
Date: 2026-10-01 10:29:57
LastEditTime: 2026-10-01 11:14:37
'''
#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        # convert the problem: we need to split the stones into to piles
        # the weight sum of each pile should be close to total_sum/2
        # assume we have a bag with capacity sum/2, what is the max_weight it can pack
        n = len(stones)
        total_sum = sum(stones)
        # round to floor means we choose the pile <= total_sum / 2
        capacity = int(total_sum / 2)

        # Method 2: DP, optimize method 1
        # space complexity: O(capacity)
        dp = [0] * (capacity + 1)
        for i, w in enumerate(stones):
            # reverse update, because we need old dp[j-w]
            for j in range(capacity, -1, -1):
                if j >= w:
                    dp[j] = max(dp[j], dp[j-w]+w)

        max_w = dp[capacity]

        return (total_sum - max_w) - max_w

        # Method 1: DP
        # time complexity: O(n* capacity)
        # space complexity: O(n * capacity)
        # dp[i][j]: the max weight of stones[:i+1] given capacity j
        dp = [[0] * (capacity+1) for _ in range(n+1)]
        # if the capacity is 0, the max weight is 0
        # if there is no stone, the max weight is 0
        for i, w in enumerate(stones, start=1):
            for j in range(capacity+1):
                # if the capacity is not enought for current stone
                if j < w:
                    # stones[:i+1] should at least be as good as stones[:i]
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+w)
        
        max_w = max(dp[n])
        # the difference of two piles
        ans = (total_sum - max_w) - max_w

        return ans

# @lc code=end

