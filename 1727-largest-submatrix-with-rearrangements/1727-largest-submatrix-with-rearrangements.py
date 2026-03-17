from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Build heights
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        
        # Step 2: Process each row
        for i in range(m):
            row = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                height = row[j]
                width = j + 1
                max_area = max(max_area, height * width)
        
        return max_area