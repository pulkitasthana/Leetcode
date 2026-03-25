from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        # if total sum is odd → can't split equally
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # check horizontal cut
        running_sum = 0
        for i in range(m - 1):  # must leave at least one row below
            running_sum += sum(grid[i])
            if running_sum == target:
                return True
        
        # compute column sums
        col_sum = [0] * n
        for i in range(m):
            for j in range(n):
                col_sum[j] += grid[i][j]
        
        # check vertical cut
        running_sum = 0
        for j in range(n - 1):  # must leave at least one column right
            running_sum += col_sum[j]
            if running_sum == target:
                return True
        
        return False