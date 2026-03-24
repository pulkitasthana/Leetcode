from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        
        n, m = len(grid), len(grid[0])
        
        # Step 1: flatten grid
        arr = []
        for row in grid:
            arr.extend(row)
        
        size = len(arr)
        
        # Step 2: prefix product
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        # Step 3: suffix product
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        # Step 4: result array
        result = [(prefix[i] * suffix[i]) % MOD for i in range(size)]
        
        # Step 5: convert back to matrix
        ans = []
        index = 0
        
        for i in range(n):
            row = []
            for j in range(m):
                row.append(result[index])
                index += 1
            ans.append(row)
        
        return ans