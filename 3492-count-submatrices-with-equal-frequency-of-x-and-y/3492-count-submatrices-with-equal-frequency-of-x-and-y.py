from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Convert grid
        val = [[0]*n for _ in range(m)]
        hasX = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    val[i][j] = 1
                    hasX[i][j] = 1
                elif grid[i][j] == 'Y':
                    val[i][j] = -1
        
        # Prefix sums
        prefix = [[0]*(n+1) for _ in range(m+1)]
        prefixX = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = (
                    val[i][j]
                    + prefix[i][j+1]
                    + prefix[i+1][j]
                    - prefix[i][j]
                )
                
                prefixX[i+1][j+1] = (
                    hasX[i][j]
                    + prefixX[i][j+1]
                    + prefixX[i+1][j]
                    - prefixX[i][j]
                )
        
        ans = 0
        
        # Only submatrices starting at (0,0)
        for i in range(m):
            for j in range(n):
                total = prefix[i+1][j+1]
                countX = prefixX[i+1][j+1]
                
                if total == 0 and countX > 0:
                    ans += 1
        
        return ans