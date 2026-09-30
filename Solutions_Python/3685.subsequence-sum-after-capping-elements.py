'''
Author: Hannah
Date: 2026-09-30 10:31:25
LastEditTime: 2026-09-30 13:45:01
'''
#
# @lc app=leetcode id=3685 lang=python3
#
# [3685] Subsequence Sum After Capping Elements
#

# @lc code=start
class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        ans = [False] * n

        # Method 3: DP + bitset + sort
        # time complexity: O(nk/w+nlogn+min(n^2,klogn))
        # space complexity: O(k/w)
        # sort: O(nlogn)
        nums.sort()

        n = len(nums)
        ans = [False] * n
        dp = 1
        bit_mask = (1 << (k + 1)) - 1

        i = 0
        for x in range(1, n + 1):
            # only consider the number equal x
            while i < n and nums[i] == x:
                dp |= (dp << nums[i]) & bit_mask
                i += 1

            if dp >> k & 1:
                ans[x - 1:] = [True] * (n - x + 1)
                break

            # select j x from the numbers that larger than x
            for j in range(min(n - i, k // x) + 1):
                if dp >> (k - j * x) & 1:
                    ans[x - 1] = True
                    break
        return ans


        # Method 2: DP + bitset
        # time complexity: O(nk/w + nlogn)
        # We only care about sums up to k, so the length of binary is at most k+1
        # This mask prevents the integer from growing unnecessarily large.
        mask = (1 << (k + 1)) - 1
        target_bit = 1 << k
        
        for x in range(1, n + 1):
            # The 0th bit is 1, representing a sum of 0
            dp = 1
            
            for num in nums:
                cap_val = min(x, num)
                
                # Shift dp by cap_val to add the current number to all previous sums.
                # Bitwise OR merges the new sums with the old sums.
                dp = (dp | (dp << cap_val)) & mask
                
                # If the k-th bit is 1, we achieve the target sum for current x
                if dp & target_bit:
                    ans[x-1] = True
                    break
                    
        return ans
    
        # Method 1: DP. Time Limit Exceed
        # time complexity: O(n^2 k)
        # for each x, do a 0-1 packing
        for x in range(1, n+1):
            dp = [False] * (k+1)
            # corner case: no element, sum to zero
            dp[0] = True
            for i, num in enumerate(nums):
                # dp[i][j]: whether we can find a subsequence in nums[:i+1] that sum to j
                # dp[i][j] = dp[i-1,j] or dp[i-1][j-cap_val]
                cap_val = min(x, num)
                # reverse update dp, because we need old dp[j-cap_val]
                for j in range(k, cap_val-1, -1):
                    dp[j] = dp[j] or dp[j-cap_val]
                if dp[k]:
                    ans[x-1] = True
                    break
                    
        return ans

        
# @lc code=end

