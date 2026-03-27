from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        shift = k % n
        
        for i in range(m):
            row = mat[i]
            
            if i % 2 == 0:
                # even index -> left shift
                rotated = row[shift:] + row[:shift]
            else:
                # odd index -> right shift
                rotated = row[-shift:] + row[:-shift]
            
            if rotated != row:
                return False
        
        return True