'''
Author: Hannah
Date: 2026-10-02 10:36:08
LastEditTime: 2026-10-02 11:38:22
'''
#
# @lc app=leetcode id=3082 lang=python3
#
# [3082] Find the Sum of the Power of All Subsequences
#

# @lc code=start
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        # `S`: subsequence whose sum equal j
        # `T`: subsequence whose subsequences contain `S`

        # Method 4: DP, optimize method 3
        # space complexity: O(k)
        dp = [0] * (k+1)
        dp[0] = 1
        for i, num in enumerate(nums):
            for j in range(k, -1, -1):
                dp[j] = 2 * dp[j]
                if j >= num:
                    dp[j] += dp[j-num]

        return dp[k] % MOD

        # Method 3: DP
        # time complexity: O(nk)
        # space complexity: O(nk)
        # in fact, we can optimize c
        # dp[i+1][j]: the number of subsequence of nums[:i+1] whose sum eqaul j
        # if nums[i] is in T but not in S, contribute dp[i][j]
        # if nums[i] not in both T and S, contribute dp[i][j]
        # if nums[i] is in S (so in T), contribute dp[i][j-nums[i]]
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for j in range(k+1):
                dp[i+1][j] = 2 * dp[i][j]
                if j >= num:
                    dp[i+1][j] += dp[i][j-num]

        return dp[n][k] % MOD

        # Method 2: DP, optimize method 1
        # space complexity: O(nk)
        dp = [[0] * (n+1) for _ in range(k+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            num = nums[i-1]
            for j in range(k, num-1, -1):
                for c in range(n, -1, -1):
                    dp[j][c] += dp[j-num][c-1]

        cnt = sum([dp[k][c] * 2**(n-c) % MOD for c in range(n+1)])

        return cnt % MOD


        # Method 1: DP
        # time complexity: O(n^2 k)
        # space complexity: O(n^2 k)
        # if we have a subsequence S whose length is c, then the contribution of this 
        # subsequence is 2^(n-c), because for every element not in S, we can consider
        # choose it or not. So we can find all subsequnce with length c and sum equal to k
        # then sum all the possible c
        # dp[i][j][c]: the number of subsequence of nums[:i+1] whose sum is j, and has length c
        dp = [[[0] * (n+1) for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0][0] = 1
        for i in range(1, n+1):
            num = nums[i-1]
            for j in range(k+1):
                for c in range(n+1):
                    dp[i][j][c] = dp[i-1][j][c]
                    if j >= num:
                        dp[i][j][c] += dp[i-1][j-num][c-1]

        cnt = sum([dp[n][k][c] * 2**(n-c) % MOD for c in range(n+1)])

        return cnt % MOD


# @lc code=end

