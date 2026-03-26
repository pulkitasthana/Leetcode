from typing import List
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        total_sum = sum(sum(row) for row in grid)
        # Master count of all elements in the grid
        all_counts = Counter(val for row in grid for val in row)
        
        # --- Horizontal cuts ---
        if m > 1:
            top_counts = Counter()
            bottom_counts = all_counts.copy()
            top_sum = 0
            
            for i in range(m - 1):
                # Move row i into the top section
                for val in grid[i]:
                    top_sum += val
                    top_counts[val] += 1
                    bottom_counts[val] -= 1
                    if bottom_counts[val] == 0:
                        del bottom_counts[val]
                        
                bottom_sum = total_sum - top_sum
                if top_sum == bottom_sum: return True
                
                diff = abs(top_sum - bottom_sum)
                
                if top_sum > bottom_sum:
                    R = i + 1
                    # If 2D, ANY element can be removed safely without breaking connectivity
                    if R > 1 and n > 1:
                        if diff in top_counts: return True
                    # If 1D Row, only the left or right ends can be removed
                    elif R == 1:
                        if grid[0][0] == diff or grid[0][n-1] == diff: return True
                    # If 1D Column, only top or bottom ends can be removed
                    elif n == 1:
                        if grid[0][0] == diff or grid[i][0] == diff: return True
                else:
                    R = m - i - 1
                    if R > 1 and n > 1:
                        if diff in bottom_counts: return True
                    elif R == 1:
                        if grid[i+1][0] == diff or grid[i+1][n-1] == diff: return True
                    elif n == 1:
                        if grid[i+1][0] == diff or grid[m-1][0] == diff: return True

        # --- Vertical cuts ---
        if n > 1:
            left_counts = Counter()
            right_counts = all_counts.copy()
            left_sum = 0
            
            # Pre-calculate column sums for fast addition
            col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]
            
            for j in range(n - 1):
                # Move column j into the left section
                left_sum += col_sums[j]
                for r in range(m):
                    val = grid[r][j]
                    left_counts[val] += 1
                    right_counts[val] -= 1
                    if right_counts[val] == 0:
                        del right_counts[val]
                        
                right_sum = total_sum - left_sum
                if left_sum == right_sum: return True
                
                diff = abs(left_sum - right_sum)
                
                if left_sum > right_sum:
                    C = j + 1
                    if m > 1 and C > 1:
                        if diff in left_counts: return True
                    elif C == 1:
                        if grid[0][0] == diff or grid[m-1][0] == diff: return True
                    elif m == 1:
                        if grid[0][0] == diff or grid[0][j] == diff: return True
                else:
                    C = n - j - 1
                    if m > 1 and C > 1:
                        if diff in right_counts: return True
                    elif C == 1:
                        if grid[0][j+1] == diff or grid[m-1][j+1] == diff: return True
                    elif m == 1:
                        if grid[0][j+1] == diff or grid[0][n-1] == diff: return True

        return False