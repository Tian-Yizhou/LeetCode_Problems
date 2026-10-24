#
# @lc app=leetcode id=3628 lang=python3
#
# [3628] Maximum Number of Subsequences After One Inserting
#

# @lc code=start
class Solution:
    def numOfSubsequences(self, s: str) -> int:

        # Method 1: DP
        # time complexity: O(N), N=len(s)
        # space complexity: O(1)

        # `l`: the numbelr of substring l;
        # `lc`: the number of substring lc
        t = s.count('T')
        l = lc = lct = c = ct = lt = 0
        for char in s:
            if char == 'L':
                l += 1
            elif char == 'C':
                # each time encounter `c`, add lc by l
                lc += l
                c += 1
            elif char == 'T':
                # each time encounter `t`, add lct by lc, add ct by c
                lct += lc
                ct += c
                # how many `T` left on the right side of current char
                t -= 1
            # if insert `C`, the added #substring = `L` on the left side of `C` * `T` on the right side of `C`
            lt = max(lt, l * t)
        # choose the max substring in ct, lc, lt, and insert the excluded char
        return lct + max(ct, lc, lt)



# @lc code=end

