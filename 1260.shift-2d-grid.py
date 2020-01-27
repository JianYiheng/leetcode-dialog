from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid_h, grid_w = len(grid), len(grid[0])
        grid_res = []
        for i in grid:
            grid_res += i

        n = len(grid_res)
        k %= n

        grid1 = reversed(grid_res[0:n - k])
        grid2 = reversed(grid_res[n - k:])
        grid_res = list(grid1) + list(grid2)
        grid_res = list(reversed(grid_res))

        return [grid_res[i * grid_w:i * grid_w + grid_w] for i in range(grid_h)]


if __name__ == '__main__':
    ret = Solution().shiftGrid([[1], [2], [3], [4], [7], [6], [5]], 23)
    print(ret)
