#
# @lc app=leetcode id=1343 lang=python3
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # time complexity: O(n)
        # use integer to accelerate (avoid float division)
        target = k * threshold
        # initialize
        s = sum(arr[:k])
        ans = int(s >= target)
        
        # sliding window
        for i in range(k, len(arr)):
            s += arr[i] - arr[i - k]
            if s >= target:
                ans += 1
                
        return ans

# @lc code=end

