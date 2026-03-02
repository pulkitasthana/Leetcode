from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: count trailing zeros for each row
        trailing = []
        for row in grid:
            count = 0
            for num in reversed(row):
                if num == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: greedy placement
        for i in range(n):
            required = n - i - 1
            j = i
            
            # find first valid row
            while j < n and trailing[j] < required:
                j += 1
            
            if j == n:
                return -1
            
            # bubble up
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps
        