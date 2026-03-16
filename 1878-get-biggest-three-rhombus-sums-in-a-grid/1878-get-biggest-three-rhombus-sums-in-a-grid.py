from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):

                # radius 0 rhombus
                sums.add(grid[i][j])

                k = 1
                while True:
                    if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                        break

                    total = 0

                    # top -> right
                    x, y = i-k, j
                    for d in range(k):
                        total += grid[x+d][y+d]

                    # right -> bottom
                    x, y = i, j+k
                    for d in range(k):
                        total += grid[x+d][y-d]

                    # bottom -> left
                    x, y = i+k, j
                    for d in range(k):
                        total += grid[x-d][y-d]

                    # left -> top
                    x, y = i, j-k
                    for d in range(k):
                        total += grid[x-d][y+d]

                    sums.add(total)
                    k += 1

        return sorted(sums, reverse=True)[:3]