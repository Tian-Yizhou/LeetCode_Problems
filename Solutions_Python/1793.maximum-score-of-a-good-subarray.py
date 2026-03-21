'''
Author: Hannah
Date: 2026-03-20 22:43:28
LastEditTime: 2026-03-21 00:56:23
'''
#
# @lc app=leetcode id=1793 lang=python3
#
# [1793] Maximum Score of a Good Subarray
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        # Method 2: make the array "peak shape"
        n = len(nums)
        ans = nums[k]
        # L[i]: the min height in [i, k]
        L = [0] * n
        L[k] = nums[k]
        for i in range(k - 1, -1, -1):
            L[i] = min(nums[i], L[i+1])
            
        # R[j]: the min height in [k, j]
        R = [0] * n
        R[k] = nums[k]
        for j in range(k + 1, n):
            R[j] = min(nums[j], R[j-1])

        # two pointers from both end
        i, j = 0, n - 1
        
        while i <= k <= j:
            # the height of [i, j]
            h = min(L[i], R[j])
            ans = max(ans, h * (j - i + 1))
            
            # greedy: move the pointer of the lower side
            # if you move the higher side, the hight still depend on the lower side
            # and the width decreases
            if L[i] < R[j]:
                i += 1
            else:
                j -= 1
                
        return ans
        

        # Method 1: Two pointers
        n = len(nums)
        # ans at least is the height of nums[k]
        ans = nums[k]
        min_h = nums[k]
        
        # start from nums[k] to left end and right end
        i, j = k, k
        # we need to move n-1 times in total (start at nums[k])
        for _ in range(n-1):
            # if j achieves the right end
            # or i doesn't achieve the left end, and num[i-1] > nums[j+1]
            if j == n-1 or (i != 0 and nums[i-1] > nums[j+1]):
                # move i to i-1
                i -= 1
                min_h = min(min_h, nums[i])
            # Otherwise, we can only move j to j+1
            else:
                j += 1
                min_h = min(min_h, nums[j])
            # update max ans
            ans = max(ans, min_h * (j - i + 1))
            
        return ans


# @lc code=end

