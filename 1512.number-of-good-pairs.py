#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            x = nums[i]
            for j in range(i+1, n):
                y = nums[j]
                if x == y:
                    ans += 1
                else:
                    continue

        return ans
# @lc code=end

