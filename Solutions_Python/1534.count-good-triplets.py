#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#

# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0

        for i in range(n-2):
            x = arr[i]
            for j in range(i+1, n-1):
                y = arr[j]
                for k in range(j+1, n):
                    z = arr[k]
                    if abs(x - y) <= a and abs(y - z) <= b and abs(x - z) <= c:
                        ans += 1
                    else:
                        continue

        return ans
# @lc code=end

