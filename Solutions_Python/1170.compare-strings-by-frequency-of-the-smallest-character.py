'''
Author: Hannah
Date: 2026-09-30 18:42:04
LastEditTime: 2026-09-30 19:21:41
'''
#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#

# @lc code=start
# import bisect
class Solution:
    # self-defined bisect_right function. Find the smallest idx s.t. arr[idx] > x
    def upper_bound(self, arr, x):
        n = len(arr)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            # when arr[mid]=x, continue search mid's right
            if arr[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:

        n = len(queries)

        # Method: bisect_right
        # time complexity: O((W + Q) \cdot L \log L + (W + Q) \log W)
        # space complexity: O(W + Q)
        
        # convert the string into a list and sort it ascendingly
        # use bisect_right to count the frequency of lexicographically smallest character
        def f(s):
            letters = sorted(list(s), reverse=False)
            target = letters[0]
            # cnt = idx - 0 = idx
            cnt = self.upper_bound(letters, target)
            # or we can use bisect_right package
            # cnt = bisect.bisect_right(letters, target)
            return cnt

        ans = [0] * n
        # compute the frequency of words to avoid duplicate
        word_freq = [f(w) for w in words]
        word_freq.sort()
        for i, query in enumerate(queries):
            f_q = f(query)
            # we can use bisect_right again to avoid iteration
            idx = self.upper_bound(word_freq, f_q)
            cnt = len(word_freq) - idx
            ans[i] = cnt

        return ans

        
# @lc code=end

