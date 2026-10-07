'''
Author: Hannah
Date: 2026-10-07 17:07:30
LastEditTime: 2026-10-07 17:59:15
'''
#
# @lc app=leetcode id=2271 lang=python3
#
# [2271] Maximum White Tiles Covered by a Carpet
#

# @lc code=start
class Solution:
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        # Method: Sliding window
        # time complexity: O(NlogN), which is the sorting bottleneck
        # space complexity: O(1)
        tiles.sort(key=lambda x: x[0])
        ans = 0
        cover = 0
        left = 0
        # assume we put the right end of the carpet on tile_r
        for tile_l, tile_r in tiles:
            # the new covered white tiles
            cover += tile_r - tile_l + 1
            # the left end of carpet
            carpet_left = tile_r - carpetLen + 1
            # remove the tiles whose right end exceeds the left end of carpet
            while tiles[left][1] < carpet_left:
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            # if the left end of carpet is within tile[left]
            # we need to reduce the part exceed carpet left end
            uncover = max(0, carpet_left - tiles[left][0])
            # update answer for current tile's right end
            ans = max(ans, cover-uncover)

        return ans
# @lc code=end

