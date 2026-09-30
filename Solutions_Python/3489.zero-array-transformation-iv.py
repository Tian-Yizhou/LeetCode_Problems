#
# @lc app=leetcode id=3489 lang=python3
#
# [3489] Zero Array Transformation IV
#

# @lc code=start
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        # Method 2: biset
        # time complexity: O(nqM/w), n is len(nums), q is len(queries), M is max(nums)
        # space complexity: O(M/w), w is 32 or 64
        # use a binary int, if the j-th digit is 1, means we can use some queries to sum to j
        ans = 0
        for i, x in enumerate(nums):
            if x == 0:
                continue
            f = 1
            for k, (l, r, val) in enumerate(queries):
                if not l <= i <= r:
                    continue
                # f << val: choose queries[k] and add the value
                f = f | f << val
                # if the x-th digit is 1, then the number can be decreased
                if f >> x & 1:
                    ans = max(ans, k+1)
                    break
            else:
                return -1

        return ans
        
        
        # Method 1: DP
        # time complexity: O(nqM), n is len(nums), q is len(queries), M is max(nums)
        # space complexity: O(M)
        # do a selection 0-1 packing for each number in nums
        # time complexity
        # space complexity
        ans = 0
        for i, num in enumerate(nums):
            # if the number is already 0, no need to justify
            if num == 0:
                continue
            # dp[val] = True: means value `val` can be decreased
            dp = [True] + [False] * num
            for k, (l, r, val) in enumerate(queries):
                # if index `i` is not within range [l, r], cannot decrease the value
                if not l <= i <= r:
                    continue
                # reverse update so the dp[j-val] is
                for j in range(num, val-1, -1):
                    dp[j] = dp[j] or dp[j-val]
                # if num can be decreased to 0, update answer
                if dp[num]:
                    ans = max(ans, k+1)
                    break
            # otherwise, cannot decrease a number to zero after loop through all queries
            else:
                return -1

        return ans
                
# @lc code=end

